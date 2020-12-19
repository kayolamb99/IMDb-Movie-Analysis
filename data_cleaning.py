import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tsplit

#Reading in the data and splitting to features and dependent variables

movies = pd.read_csv('/Users/kayode/Desktop/Side Projects/SP3_Movies/movies.csv', encoding = 'latin-1')


#Creating a column 'isMajor' which defines whether or not a movie is produced
#by one of the six major studios

movies["isMajor"] = np.where(
(movies["company"] == "Columbia Pictures Corporation") | 
        (movies["company"] == "Paramount Pictures") |
        (movies["company"] == "Twentieth Century Fox Film Corporation") |
        (movies["company"] == "Walt Disney Pictures") |
        (movies["company"] == "Warner Bros.") |
        (movies["company"] == "Universal Pictures"),
        1,0)

#Creating a column 'budgetReturn' which approximates the sales return on each
#dollar invested in a movie

movies["budgetReturn"] = movies["gross"] / movies["budget"]

#Creating a column 'isLong' which defines whether or not a movie is a long 
#(greater than the standard 120 minutes)

movies["isLong"] = np.where((movies["runtime"] > 120), 1,0)

#Creating an analagous column 'isShort' which defines whether or not a movie is 
# short (less than the standard 75 minutes minimum)

movies["isShort"] = np.where((movies["runtime"] < 75),1,0)


#Splitting Data into training and testing
movies_train, movies_test = tsplit(movies, test_size = 0.2, random_state = 1)

#Moving columns to more appropriate locations
movies = movies[['name','genre', 'rating' , 'country', 'company', 'isMajor',
                 'released', 'year', 'runtime', 'isLong', 'isShort',
                 'score', 'votes', 'star', 'director', 
                 'budget', 'gross', 'budgetReturn']]

#Removing duplicates, none found with below function
movies.duplicated()

#Splitting data into features (indepedent variables) and response 
#(dependet variable)
features1 = movies.loc[:,"name":"budget"]
features2 = movies.loc[:,"budgetReturn"]
features = pd.concat([features1, features2],axis = 1)
dependent = movies.loc[:,"gross"]

#Writing new datasets to csv files
movies.to_csv('/Users/kayode/Desktop/Side Projects/SP3_Movies/movies_clean.csv')
features.to_csv('/Users/kayode/Desktop/Side Projects/SP3_Movies/features.csv')
dependent.to_csv('/Users/kayode/Desktop/Side Projects/SP3_Movies/dependent.csv')


