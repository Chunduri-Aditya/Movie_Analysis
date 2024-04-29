"""
Clean the data, transform the data and store the files in the data/processed folder

Author: Chunduri Aditya
"""
import pandas as pd
import json

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
    # Rename columns to align with each other
    rename_columns(imdb_movies_list, {"Movie Name": "movie_title"})
    rename_columns(movie_reviews, {"movie_name": "movie_title"})
    rename_columns(movies_metadata, {"title": "movie_title"})
    
    # Extract and clean genres
    movies_metadata['cleaned_genres'] = movies_metadata['genres'].apply(extract_genres)
    
    # Select columns to keep
    columns_to_keep = ['movie_title', 'budget', 'revenue', 'year', 'runtime', 'vote_average', 'vote_count', 'cleaned_genres']
    final_data = movies_metadata[columns_to_keep]
    
    return final_data

def main():
    # Read data from input files
    imdb_movies_list = pd.read_csv('data/raw/imdb_movies_list.csv')
    movie_reviews = pd.read_csv('data/raw/movie_reviews.csv')
    movies_metadata = pd.read_csv('data/raw/movies_metadata_kaggle.csv', low_memory=False)
    
    # Clean data
    cleaned_data = clean_data(imdb_movies_list, movie_reviews, movies_metadata)
    cleaned_data.to_csv('data/processed/final_data_cleaned.csv', index=False)

if __name__ == "__main__":
    main()

