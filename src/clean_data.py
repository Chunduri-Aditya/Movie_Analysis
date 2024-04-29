"""
Clean the data, transform it, and store the files in the data/processed folder.
Assumes that the raw data is available in the data/raw folder.

Author: Chunduri Aditya
"""
import pandas as pd
import json
import os

def rename_columns(df, new_column_names):
    df.rename(columns=new_column_names, inplace=True)

def extract_genres(genres_str):
    try:
        genres_list = json.loads(genres_str.replace("'", '"'))
        genres_names = [genre['name'] for genre in genres_list]
        return ", ".join(genres_names)
    except Exception as e:
        print(f"Error extracting genres: {e}")
        return None

def clean_data(imdb_movies_list, movie_reviews, movies_metadata):
    rename_columns(imdb_movies_list, {"Movie Name": "movie_title"})
    rename_columns(movie_reviews, {"movie_name": "movie_title"})
    rename_columns(movies_metadata, {"title": "movie_title"})

    movies_metadata['cleaned_genres'] = movies_metadata['genres'].apply(extract_genres)
    columns_to_keep = ['movie_title', 'budget', 'revenue', 'year', 'runtime', 'vote_average', 'vote_count', 'cleaned_genres']
    final_data = movies_metadata[columns_to_keep]
    return final_data

def main():
    raw_data_dir = 'data/raw'
    processed_data_dir = 'data/processed'
    os.makedirs(processed_data_dir, exist_ok=True)

    imdb_movies_list = pd.read_csv(os.path.join(raw_data_dir, 'imdb_movies_list.csv'))
    movie_reviews = pd.read_csv(os.path.join(raw_data_dir, 'movie_reviews.csv'))
    movies_metadata = pd.read_csv(os.path.join(raw_data_dir, 'movies_metadata_kaggle.csv'), low_memory=False)

    cleaned_data = clean_data(imdb_movies_list, movie_reviews, movies_metadata)
    cleaned_data.to_csv(os.path.join(processed_data_dir, 'final_data_cleaned.csv'), index=False)

if __name__ == "__main__":
    main()
