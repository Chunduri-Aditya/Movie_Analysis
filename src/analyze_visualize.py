"""
Analyze and visualize the data to answer the project-specific questions.
Assumes that the processed data is available in the data/processed folder.

Author: Chunduri Aditya
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from wordcloud import WordCloud

def generate_wordcloud(data, title):
    text = ' '.join(review for review in data)
    wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

def analyze_visualize(final_data):
    # Histogram of movie ratings
    plt.figure(figsize=(10, 6))
    plt.hist(final_data['rating'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Movie Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Extract genres into a list of strings
    genre_list = [genre for sublist in final_data['cleaned_genres'].dropna().str.split(', ') for genre in sublist]
    genres_df = pd.DataFrame({'Genre': genre_list})

    # Countplot of genres
    plt.figure(figsize=(12, 7))
    sns.countplot(data=genres_df, y='Genre', order=genres_df['Genre'].value_counts().index[:10], palette='viridis')
    plt.title('Top 10 Genres by Number of Movies')
    plt.xlabel('Number of Movies')
    plt.ylabel('Genre')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

    # Scatter plot of Budget vs Revenue
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=final_data, x='budget', y='revenue', alpha=0.6, color='darkblue')
    plt.title('Budget vs. Revenue')
    plt.xlabel('Budget (in billions)')
    plt.ylabel('Revenue (in billions)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
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

    # Correlation matrix heatmap
    numeric_cols = ['rating', 'budget', 'revenue', 'runtime', 'vote_average', 'vote_count']
    corr_matrix = final_data[numeric_cols].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Matrix of Numeric Features')
    plt.show()

    # Sentiment analysis and visualization
    final_data['sentiment_polarity'] = final_data['review_text'].apply(lambda x: TextBlob(x).sentiment.polarity if x else None)
    plt.figure(figsize=(10, 6))
    sns.histplot(final_data['sentiment_polarity'], bins=30, color='purple', kde=True)
    plt.title('Distribution of Sentiment Polarity in Movie Reviews')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def main():
    processed_data_dir = 'data/processed'
    data_file = os.path.join(processed_data_dir, 'final_data.csv')
    
    # Read processed data
    final_data = pd.read_csv(data_file)
    
    # Perform analysis and visualization
    analyze_visualize(final_data)

if __name__ == "__main__":
    main()
