"""
Integrates all the data into a format that can be easily analyzed
This will probably take the form of merging (joining) several Pandas
DataFrames, or issuing SQL queries over tables in a relational DB.

Author: < Chunduri Aditya >
"""
import pandas as pd
import os

def merge_data(imdb_movies_list, movie_reviews, movies_metadata):
    # Merge dataframes
    merged_reviews = pd.merge(imdb_movies_list, movie_reviews, on="movie_title", how="inner")
    final_merged_data = pd.merge(merged_reviews, movies_metadata, on="movie_title", how="inner")
    return final_merged_data

def main():
    # Read data from input files
    imdb_movies_list = pd.read_csv('data/raw/imdb_movies_list.csv')
    movie_reviews = pd.read_csv('data/raw/movie_reviews.csv')
    movies_metadata = pd.read_csv('data/raw/movies_metadata_kaggle.csv', low_memory=False)
    
    # Merge data
    integrated_data = merge_data(imdb_movies_list, movie_reviews, movies_metadata)
    
    # Save integrated data
    integrated_data.to_csv('data/processed/final_data.csv', index=False)

if __name__ == "__main__":
    main()

