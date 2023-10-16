# penguins.py
# Author: Sean Humphreys
# Solution to Task two on the Fundamentals of Data Analysis module 2023. Task - "give an overview
# of the famous penguins data set,2 explaining the types of variables it contains. Suggest the
# types of variables that should be used to model them in Python, explaining your rationale.""

# ref - https://medium.com/@marvelouskgc/build-a-penguin-project-using-pandas-and-seaborn-eugene-tsai-e4b7e0b499ea

# import the pandas module used to read in the data set file as a data frame
import pandas as pd
import seaborn as sns
penguins = sns.load_dataset('penguins')

# check penguins is a pandas DataFrame
print(type(penguins))
print('\n')

# print the first five rows of the dataset
print(penguins.head())
print('\n')

# print a summary of the null values
print(penguins.isnull().sum())
print('\n')

