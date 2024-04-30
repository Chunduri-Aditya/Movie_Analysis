"""
Analyze and visualize the data to answer the project-specific questions.
Assumes that the processed data is available in the data/processed folder.

Author: Chunduri Aditya
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob


def calculate_sentiment(text):
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return None


def analyze_visualize(final_data):
    if 'sentiment_polarity' not in final_data.columns:
        final_data['sentiment_polarity'] = final_data['review_text'].apply(calculate_sentiment)

    if 'sentiment_polarity_avg' not in final_data.columns:
        final_data['sentiment_polarity_avg'] = final_data.groupby('movie_title')['sentiment_polarity'].transform('mean')

    expanded_genres = final_data['cleaned_genres'].dropna().str.split(', ').apply(pd.Series).stack().reset_index(
        level=1, drop=True)
    genre_sentiment = final_data.join(expanded_genres.rename('Genre'))
    genre_sentiment.reset_index(drop=True, inplace=True)  # Resetting index to prevent duplicate labels

    # Filter for top genres
    top_genres = genre_sentiment['Genre'].value_counts().index[:10]
    filtered_genre_sentiment = genre_sentiment[genre_sentiment['Genre'].isin(top_genres)]
    filtered_genre_sentiment.reset_index(drop=True, inplace=True)  # Resetting index again to ensure no duplicates

    # Histogram of movie ratings
    plt.figure(figsize=(10, 6))
    plt.hist(final_data['rating'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Movie Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Average movie rating over the years
    average_rating_per_year = final_data.groupby('year')['rating'].mean().reset_index()
    plt.figure(figsize=(12, 7))
    sns.lineplot(data=average_rating_per_year, x='year', y='rating', marker='o', linestyle='-', color='maroon')
    plt.title('Average Movie Rating Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Average Rating')
    plt.grid(True)
    plt.show()

    # Histogram of sentiment polarity in movie reviews
    plt.figure(figsize=(10, 6))
    sns.histplot(final_data['sentiment_polarity'], bins=30, color='purple', kde=True)
    plt.title('Distribution of Sentiment Polarity in Movie Reviews')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Distribution of Sentiment Polarity by Genre
    plt.figure(figsize=(14, 8))
    sns.boxplot(data=filtered_genre_sentiment, x='sentiment_polarity', y='Genre', hue='Genre', palette='autumn',
                dodge=False)
    plt.legend().remove()  # Removes the legend, as it is redundant in this context
    plt.title('Distribution of Sentiment Polarity by Genre')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Genre')
    plt.grid(True)
    plt.show()

    # Average Sentiment Polarity vs. Revenue
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=final_data, x='sentiment_polarity_avg', y='revenue', alpha=0.6, color='red')
    plt.title('Average Sentiment Polarity vs. Revenue')
    plt.xlabel('Average Sentiment Polarity')
    plt.ylabel('Revenue')
    plt.yscale('log')
    plt.grid(True)
    plt.show()

    # KDE plot for sentiment polarity distribution for top and bottom rated movies
    top_rated_threshold = final_data['rating'].quantile(0.90)
    bottom_rated_threshold = final_data['rating'].quantile(0.10)
    top_rated_movies = final_data[final_data['rating'] >= top_rated_threshold]
    bottom_rated_movies = final_data[final_data['rating'] <= bottom_rated_threshold]

    plt.figure(figsize=(12, 6))
    sns.kdeplot(top_rated_movies['sentiment_polarity'], label='Top Rated Movies', fill=True)
    sns.kdeplot(bottom_rated_movies['sentiment_polarity'], label='Bottom Rated Movies', fill=True)
    plt.title('Sentiment Polarity Distribution for Top and Bottom Rated Movies')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

    # Scatter plot with a regression line for sentiment polarity vs. IMDb ratings
    average_sentiment_per_movie = final_data.groupby('movie_title')['sentiment_polarity'].mean().reset_index()
    movie_ratings_sentiments = final_data[['movie_title', 'rating']].drop_duplicates().merge(
        average_sentiment_per_movie, on='movie_title')

    plt.figure(figsize=(10, 6))
    sns.regplot(x='sentiment_polarity', y='rating', data=movie_ratings_sentiments, scatter_kws={'alpha': 0.5},
                line_kws={'color': 'red'})
    plt.title('Relationship Between Sentiment Polarity and IMDb Ratings')
    plt.xlabel('Average Sentiment Polarity')
    plt.ylabel('IMDb Rating')
    plt.grid(True)
    plt.show()


def main():
    data_file = 'data/processed/final_data.csv'

    # Read processed data
    final_data = pd.read_csv(data_file)

    # Perform analysis and visualization
    analyze_visualize(final_data)


if __name__ == "__main__":
    main()
