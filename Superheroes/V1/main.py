### This is my first attempt at generating a graph given CSV.
### I'm using a sample CSV I found from an open-source, FiveThirtyEight 
### They make the data sets used in its articles available online on Github.
### Alot of my data sets will likely come from here.

import pandas as pd 
import matplotlib.pyplot as plt    

# read in the csv file from the folder
character_data = pd.read_csv('/Users/meetkothari/Desktop/coding/python/Data_Analytics/v1/comic_data.csv')

# make sure the file was import correctly
print(character_data.head())

# get a handle on the data
print(character_data.info())

# first attempt at making a graph to show the breakdown of male to female superheroes
character_data['SEX'].value_counts().plot(kind='pie', figsize=(20, 6))

plt.show()
