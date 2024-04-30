"""
Prepares datasets by cleaning and transforming them for easy integration in subsequent analysis steps.
Author: Chunduri Aditya
"""
import pandas as pd
import os
import json


def clean_data(dataset_path, rename_map, genre_column=None):
    """
    Loads, cleans, and transforms a dataset. Renames columns, extracts genres if specified, and returns the cleaned dataframe.
    """
    try:
        df = pd.read_csv(dataset_path)
    except FileNotFoundError:
        print(f"File not found: {dataset_path}")
        return None

    # Rename columns
    df.rename(columns=rename_map, inplace=True)

    # Extract genres if a column name for genres is provided
    if genre_column and genre_column in df.columns:
        df['cleaned_genres'] = df[genre_column].apply(extract_genres)
        df.drop(columns=[genre_column], inplace=True)  # Remove original genre column

    return df


def extract_genres(genres_str):
    """
    Converts JSON string of genres into a comma-separated string of genre names.
    """
    try:
        genres_list = json.loads(genres_str.replace("'", '"'))
        return ", ".join(genre['name'] for genre in genres_list)
    except json.JSONDecodeError as e:
        print(f"Failed to decode genres: {e}")
        return None


def main():
    """
    Main function to handle cleaning of individual datasets.
    """
    raw_data_dir = 'data/raw'
    processed_data_dir = 'data/processed'

    # Ensure the processed data directory exists
    os.makedirs(processed_data_dir, exist_ok=True)

    # Define mappings and configurations for each dataset
    configurations = [
        {'path': os.path.join(raw_data_dir, 'imdb_movies_list.csv'), 'rename_map': {'Movie Name': 'movie_title'},
         'genre_column': None},
        {'path': os.path.join(raw_data_dir, 'movie_reviews.csv'), 'rename_map': {'movie_name': 'movie_title'},
         'genre_column': None},
        {'path': os.path.join(raw_data_dir, 'movies_metadata_kaggle.csv'), 'rename_map': {'title': 'movie_title'},
         'genre_column': 'genres'}
    ]

    # Process each dataset according to its configuration
    for config in configurations:
        cleaned_data = clean_data(config['path'], config['rename_map'], config['genre_column'])
        if cleaned_data is not None:
            output_path = os.path.join(processed_data_dir, os.path.basename(config['path']))
            cleaned_data.to_csv(output_path, index=False)
            print(f"Cleaned data saved to {output_path}")


if __name__ == "__main__":
    main()
