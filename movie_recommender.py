import pandas as pd
import numpy as np
import sklearn
import seaborn
import re

movies = pd.read_csv('Movie_Recommender/ml-32m/movies.csv')
ratings = pd.read_csv('Movie_Recommender/ml-32m/ratings.csv')

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


