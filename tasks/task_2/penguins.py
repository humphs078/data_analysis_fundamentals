0000# penguins.py
# Author: Sean Humphreys
# Task 2 on the Fundamentals of Data Analysis module 2023. Task - "give an overview
# of the famous penguins data set,2 explaining the types of variables it contains. Suggest the
# types of variables that should be used to model them in Python, explaining your rationale."
# This script will output a brief summary of the variables in the Penguins dataset

# import the pandas module used to read in the data set file as a data frame
import pandas as pd
import seaborn as sns
penguins = sns.load_dataset('penguins')

# Define variables
ds_name = "Penguins dataset"
rows = penguins.shape[0]
columns = penguins.shape[1]
ds_type = type(penguins)
null_values = penguins.isnull().sum()
ds_5_rows = penguins.head()
species = penguins['species'].unique()
islands = penguins['island'].unique()
sex = penguins['sex'].unique()


# print formatted string with information on dataset
print(f'\nThe {ds_name} consists of {rows} rows and {columns} columns.\n' 
      f'\nThe python DataType of the {ds_name} is {ds_type}.\n'
      f'\n{ds_name} Null Value summary: \n{null_values}\n'
      f'\n{ds_name} DataType Summary:')

penguins.info()


# print the first five rows of the dataset
print(f'\nThe first 5 rows of the {ds_name} are:\n'
      f'{ds_5_rows}')

# print information on the categorical variables in the dataset
print(f'\n***Categorical Variables***'
      f'\nThe species of penguins in the \"species\" are '
      f'{species[0]}, {species[1]} and {species[2]}.'
      f'\nThe islands in the \"islands\" variable are'
      f' {islands[0]}, {islands[1]} and {islands[2]}.'
      f'\nThe sex variables are {sex[0]} and {sex[1]}.')

# print information on the continuous variables
print(f'\n***Continuous Variables***\n'
      f'The continuous variables in the dataset are'
      f' \"Bill Length\", \"Bill Depth" and \"Flipper Length\".')