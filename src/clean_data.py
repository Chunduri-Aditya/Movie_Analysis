"""
Clean the data, transform the data and store the files in the data/processed folder

Author: < Student Name>
"""
import json

def rename_columns(df, new_column_names):
    df.rename(columns=new_column_names, inplace=True)

def extract_genres(genres_str):
    try:
        genres_list = json.loads(genres_str.replace("'", '"'))
        genres_names = [genre['name'] for genre in genres_list]
        return ", ".join(genres_names)
    except:
        return None

def clean_data(imdb_movies_list, movie_reviews, movies_metadata):
    rename_columns(imdb_movies_list, {"Movie Name": "movie_title"})
    rename_columns(movie_reviews, {"movie_name": "movie_title"})
    rename_columns(movies_metadata, {"title": "movie_title"})
    
    merged_reviews = pd.merge(imdb_movies_list, movie_reviews, on="movie_title", how="inner")
    final_merged_data = pd.merge(merged_reviews, movies_metadata, on="movie_title", how="inner")

    final_merged_data['cleaned_genres'] = final_merged_data['genres'].apply(extract_genres)
    
    columns_to_keep = [
        'movie_title', 'rating', 'genres', 'budget', 'revenue', 
        'review_text', 'year', 'runtime', 'vote_average', 'vote_count', 'cleaned_genres'
    ]
    
    final_data = final_merged_data[columns_to_keep]
    final_data.to_csv('data/processed/final_data.csv', index=False)
    return final_data

