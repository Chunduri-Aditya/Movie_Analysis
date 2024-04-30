"""
Merges cleaned datasets into a single DataFrame for further analysis and cleans up intermediate files.
Author: Chunduri Aditya
"""
import pandas as pd
import os


def load_data(file_path):
    """
    Loads a dataset from a specified file path.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None


def merge_datasets(dataframes, key='movie_title'):
    """
    Merges multiple dataframes on a specified key using inner join.
    """
    if not dataframes:
        return None

    # Start with the first dataframe
    final_data = dataframes[0]

    # Merge each subsequent dataframe
    for df in dataframes[1:]:
        final_data = pd.merge(final_data, df, on=key, how='inner')

    return final_data


def cleanup_files(directory, keep_file):
    """
    Deletes all files in the specified directory except for the keep_file.
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename != keep_file:
            os.remove(file_path)
            print(f"Deleted {file_path}")


def main():
    """
    Main function to merge cleaned datasets stored in the processed data directory and cleanup intermediate files.
    """
    processed_data_dir = 'data/processed'
    file_names = ['imdb_movies_list.csv', 'movie_reviews.csv', 'movies_metadata_kaggle.csv']
    dataframes = []

    # Load each dataset
    for file_name in file_names:
        file_path = os.path.join(processed_data_dir, file_name)
        df = load_data(file_path)
        if df is not None:
            dataframes.append(df)
        else:
            print(f"Skipping missing file: {file_name}")

    # Merge all loaded dataframes
    final_data = merge_datasets(dataframes)
    if final_data is not None:
        final_data_path = os.path.join(processed_data_dir, 'final_data.csv')
        final_data.to_csv(final_data_path, index=False)
        print(f"Final merged data saved to {final_data_path}")

        # Clean up all intermediate files, keeping only the final_data.csv
        cleanup_files(processed_data_dir, 'final_data.csv')
    else:
        print("Failed to merge data due to missing datasets.")


if __name__ == "__main__":
    main()
