import pandas as pd
import numpy as np
import sklearn
import seaborn
import re

movies = pd.read_csv('Movie_Recommender/ml-32m/movies.csv')
ratings = pd.read_csv('Movie_Recommender/ml-32m/ratings.csv')
tags = pd.read_csv('Movie_Recommender/ml-32m/tags.csv')

def get_year(title):
    match = re.search(r'\((\d{4})\)', title)
    if match: 
        return int(match.group(1))
    return None

#adding a year column to the movies dataframe
movies['year']= movies['title'].apply(get_year)

