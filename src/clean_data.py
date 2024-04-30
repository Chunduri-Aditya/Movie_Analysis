# Import Libraries
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import os


# Functions for Data Processing

def extract_genres(genres_str):
    """Converts JSON string of genres into a comma-separated string of genre names."""
    try:
        genres_list = json.loads(genres_str.replace("'", '"'))
        return ", ".join(genre['name'] for genre in genres_list)
    except json.JSONDecodeError:
        return None


def rename_columns(df, new_column_names):
    """Renames columns in a DataFrame according to a dictionary mapping."""
    df.rename(columns=new_column_names, inplace=True)
    return df


def clean_data(imdb_movies_list, movie_reviews, movies_metadata):
    """Cleans and merges multiple datasets into a final DataFrame."""
    imdb_movies_list = rename_columns(imdb_movies_list, {"Movie Name": "movie_title"})
    movie_reviews = rename_columns(movie_reviews, {"movie_name": "movie_title"})
    movies_metadata = rename_columns(movies_metadata, {"title": "movie_title"})

    movies_metadata['cleaned_genres'] = movies_metadata['genres'].apply(extract_genres)

    # Merging datasets
    merged_reviews = pd.merge(imdb_movies_list, movie_reviews, on="movie_title", how="inner")
    final_merged_data = pd.merge(merged_reviews, movies_metadata, on="movie_title", how="inner")

    columns_to_keep = [
        'movie_title', 'budget', 'revenue', 'year', 'runtime', 'vote_average', 'vote_count', 'cleaned_genres'
    ]
    final_data = final_merged_data[columns_to_keep]

    return final_data


def main():
    """Main function to run data cleaning and file storage operations."""
    raw_data_dir = 'data/raw'
    processed_data_dir = 'data/processed'
    # Loading data with exception handling
    try:
        imdb_movies_list = pd.read_csv(os.path.join(raw_data_dir, 'imdb_movies_list.csv'))
        movie_reviews = pd.read_csv(os.path.join(raw_data_dir, 'movie_reviews.csv'))
        movies_metadata = pd.read_csv(os.path.join(raw_data_dir, 'movies_metadata_kaggle.csv'), low_memory=False)
    except FileNotFoundError as e:
        print(f"Error loading data files: {e}")
        return

    # Clean and store data
    cleaned_data = clean_data(imdb_movies_list, movie_reviews, movies_metadata)
    cleaned_data.to_csv(os.path.join(processed_data_dir, 'final_data_cleaned.csv'), index=False)


if __name__ == "__main__":
    main()
