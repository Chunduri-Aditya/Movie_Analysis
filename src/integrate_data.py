"""
Integrates all the data into a format that can be easily analyzed.
This will probably take the form of merging several Pandas DataFrames.
Author: Chunduri Aditya
"""
import pandas as pd
import os

def merge_data(imdb_movies_list, movie_reviews, movies_metadata):
    merged_reviews = pd.merge(imdb_movies_list, movie_reviews, on="movie_title", how="inner")
    final_merged_data = pd.merge(merged_reviews, movies_metadata, on="movie_title", how="inner")
    return final_merged_data

def main():
    raw_data_dir = 'data/raw'
    processed_data_dir = 'data/processed'
    os.makedirs(processed_data_dir, exist_ok=True)

    imdb_movies_list = pd.read_csv(os.path.join(raw_data_dir, 'imdb_movies_list.csv'))
    movie_reviews = pd.read_csv(os.path.join(raw_data_dir, 'movie_reviews.csv'))
    movies_metadata = pd.read_csv(os.path.join(raw_data_dir, 'movies_metadata_kaggle.csv'), low_memory=False)

    integrated_data = merge_data(imdb_movies_list, movie_reviews, movies_metadata)
    integrated_data.to_csv(os.path.join(processed_data_dir, 'final_data.csv'), index=False)

if __name__ == "__main__":
    main()
