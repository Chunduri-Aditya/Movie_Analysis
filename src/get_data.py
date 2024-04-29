"""
Download the data and store it in the data/raw folder

Author: < Student Name >
"""

from src.utils.helper import helper_function_name

result = helper_function_name(argument=False)
print(result)

import pandas as pd

def main():
    # Read data from existing CSV files
    imdb_data = pd.read_csv('data/raw/imdb_movies_list.csv')
    rotten_tomatoes_data = pd.read_csv('data/raw/movie_reviews.csv')
    movies_metadata = pd.read_csv('data/raw/movies_metadata_kaggle.csv', low_memory=False)

    # Your further processing code goes here

if __name__ == "__main__":
    main()
