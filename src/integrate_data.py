"""
Integrates all the data into a format that can be easily analyzed
This will probably take the form of merging (joining) several Pandas
DataFrames, or issuing SQL queries over tables in a relational DB.

Author: < Student Name >
"""
import pandas as pd

def merge_datasets(imdb_movies_list, movie_reviews, movies_metadata):
    merged_reviews = pd.merge(imdb_movies_list, movie_reviews, on="movie_title", how="inner")
    final_merged_data = pd.merge(merged_reviews, movies_metadata, on="movie_title", how="inner")
    return final_merged_data

def prepare_final_data(final_merged_data):
    columns_to_keep = [
        'movie_title', 'rating', 'genres', 'budget', 'revenue', 
        'review_text', 'year', 'runtime', 'vote_average', 'vote_count', 'cleaned_genres'
    ]
    final_data = final_merged_data[columns_to_keep]
    final_data.to_csv('/data/processed/final_data.csv', index=False)
    return final_data
