"""
Clean the data, transform the data and store the files in the data/processed folder

Author: < Student Name>
"""
import json

def rename_columns(imdb_movies_list, movie_reviews, movies_metadata):
    imdb_movies_list.rename(columns={"Movie Name": "movie_title"}, inplace=True)
    movie_reviews.rename(columns={"movie_name": "movie_title"}, inplace=True)
    movies_metadata.rename(columns={"title": "movie_title"}, inplace=True)

def extract_genres(genres_str):
    try:
        genres_list = json.loads(genres_str.replace("'", '"'))
        genres_names = [genre['name'] for genre in genres_list]
        return ", ".join(genres_names)  
    except:
        return None

def clean_genres(final_merged_data):
    final_merged_data['cleaned_genres'] = final_merged_data['genres'].apply(extract_genres)
    return final_merged_data
