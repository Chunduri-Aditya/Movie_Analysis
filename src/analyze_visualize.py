"""
Analyze the data to answer the project specific questions

Author: < Student Name >
"""
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

    # Pairplot of selected numeric columns
    numeric_cols = ['rating', 'budget', 'revenue', 'runtime', 'vote_average', 'vote_count']
    pairplot_data = final_data[numeric_cols].dropna()
    sns.pairplot(pairplot_data)
    plt.show()

    # Boxplot of ratings by genre
    expanded_genres = final_data['cleaned_genres'].dropna().str.split(', ').apply(pd.Series).stack().reset_index(level=1, drop=True)
    genre_ratings = final_data.join(expanded_genres.rename('Genre')).reset_index()
    top_genres = genres_df['Genre'].value_counts().index[:10]
    filtered_genre_ratings = genre_ratings[genre_ratings['Genre'].isin(top_genres)]
    plt.figure(figsize=(14, 8))
    sns.boxplot(data=filtered_genre_ratings, x='rating', y='Genre', palette='cool')
    plt.title('Distribution of Ratings by Genre')
    plt.xlabel('Rating')
    plt.ylabel('Genre')
    plt.grid(True)
    plt.show()

    # Correlation matrix heatmap
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

    # Boxplot of sentiment polarity by genre
    genre_sentiment = final_data.join(expanded_genres.rename('Genre'))
    top_genres = genre_sentiment['Genre'].value_counts().index[:10]
    filtered_genre_sentiment = genre_sentiment[genre_sentiment['Genre'].isin(top_genres)]
    plt.figure(figsize=(14, 8))
    sns.boxplot(data=filtered_genre_sentiment, x='sentiment_polarity', y='Genre', palette='autumn')
    plt.title('Distribution of Sentiment Polarity by Genre')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Genre')
    plt.grid(True)
    plt.show()

    # Generate word clouds for positive and negative sentiments
    positive_reviews = final_data[final_data['sentiment_polarity'] > 0.5]['review_text']
    negative_reviews = final_data[final_data['sentiment_polarity'] < -0.5]['review_text']
    generate_wordcloud(positive_reviews, 'Word Cloud for Positive Reviews')
    generate_wordcloud(negative_reviews, 'Word Cloud for Negative Reviews')

def generate_wordcloud(data, title):
    text = ' '.join(review for review in data)
    wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()
