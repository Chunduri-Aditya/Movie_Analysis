"""
Download the data and store it in the data/raw folder.
Assumes that data is manually placed in the correct directory.

Author: Chunduri Aditya
"""

import pandas as pd
import os

def main():
    data_dir = 'data/raw'
    # Ensure the data directory exists
    os.makedirs(data_dir, exist_ok=True)

    # Read data from existing CSV files
    imdb_data = pd.read_csv(os.path.join(data_dir, 'imdb_movies_list.csv'))
    rotten_tomatoes_data = pd.read_csv(os.path.join(data_dir, 'movie_reviews.csv'))
    movies_metadata = pd.read_csv(os.path.join(data_dir, 'movies_metadata_kaggle.csv'), low_memory=False)

    # Further processing code goes here (optional)

if __name__ == "__main__":
    main()
