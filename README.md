[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/qAF9nhzI)
# Analyzing the Influence of Rotten Tomatoes Reviews on IMDb Movie Ratings

## Introduction
This project explores the potential influence of Rotten Tomatoes reviews on IMDb movie ratings. By integrating data from IMDb, Rotten Tomatoes, and Kaggle, the project utilizes web scraping, data cleaning, sentiment analysis, and visualization techniques to discern patterns and relationships that could suggest predictive connections between audience reception and cinematic success.

## Project Objectives
- To collect data related to movie ratings and reviews from IMDb and Rotten Tomatoes using automated web scraping.
- To perform sentiment analysis on Rotten Tomatoes reviews to assess their sentiment score.
- To analyze the correlation between the sentiment scores from reviews and the IMDb ratings.
- To visualize the relationships and provide insights that can help movie industry stakeholders understand audience sentiment impacts.

## Installation Instructions
To set up the project environment and run the analysis, follow these steps:

# Install required Python libraries
pip install -r requirements.txt

## Data Sources
- **IMDb Top 250 Movies**: Provides titles, years, and ratings of the top 250 movies as rated by IMDb users.
  - Data scraping method: BeautifulSoup for static content extraction.
  - Source: [IMDb Top 250](https://www.imdb.com/chart/top)

- **Rotten Tomatoes Reviews**: Contains extensive user-generated reviews and ratings.
  - Data scraping method: Selenium for dynamic content extraction.
  - Source: [Rotten Tomatoes](https://www.rottentomatoes.com)

- **Kaggle Movie Dataset**: Used for additional metadata and supplementary data.
  - Acquisition method: Download from Kaggle datasets.
  - Source: [The Movies Dataset on Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv)
  - Drive link: [Dataset used from Kaggle from the above link](https://drive.google.com/file/d/1exuG8tHxqiY7BiDZ5jKgsddOOoPIaBj2/view?usp=sharing)


## Results and Discussion
This project includes a detailed analysis report and visualizations that demonstrate the findings. The correlation between Rotten Tomatoes sentiments and IMDb ratings is discussed with statistical evidence and visual aids.

## Acknowledgments
This project is created as part of the coursework for DSCI 510 at the University of Southern California. Data used in this project is sourced from publicly available data on IMDb, Rotten Tomatoes, and Kaggle.

## Author
- Aditya Chunduri
