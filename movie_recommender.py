import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import re
import matplotlib.pyplot as plt

movies = pd.read_csv('Movie_Recommender/movie_data/movies.csv')
ratings = pd.read_csv('Movie_Recommender/movie_data/ratings.csv')

def get_year(title):
    match = re.search(r'\((\d{4})\)', title)
    if match: 
        return int(match.group(1))
    return None

#adding a year column to the movies dataframe
movies['year']= movies['title'].apply(get_year)

#don't want any decimal ending years
movies['year'] = movies['year'].astype('Int64')

#creating subset with movies since 2020
recent_movies = movies[movies['year'] >= 2020]
recent_movie_ratings = ratings[ratings['movieId'].isin(recent_movies['movieId'])]

#no null values found when doing print statements:
    #print(recent_movies.isnull().sum())
    #print(recent_movie_ratings.isnull().sum())

#checking for duplicates- none found
duplicates = recent_movies[recent_movies.duplicated(subset='movieId')]
duplicate_ratings = recent_movie_ratings[recent_movie_ratings.duplicated(subset=['userId','movieId'])]

#removing movies that have 'no genres listed' as their only genre
recent_movies = recent_movies[recent_movies['genres'] != '(no genres listed)']
recent_movie_ratings = recent_movie_ratings[recent_movie_ratings['movieId'].isin(recent_movies['movieId'])]

#Genres by count (# of movies in each genre)
genres = recent_movies['genres'].str.split('|').explode()
genre_counts = genres.value_counts()

#graphing
plt.figure(figsize=(10,8))
sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
plt.title('Genres by Count (2020-2024)')
plt.xlabel('Genres')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

#movies with greatest number of ratings
movie_ratings_count = recent_movie_ratings.groupby('movieId')['rating'].count().sort_values(ascending=False).head(5)
ratings_titles = recent_movies.set_index('movieId').loc[movie_ratings_count.index,'title']
