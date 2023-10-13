# iris.py
# Author: Sean Humphreys
# Script to investigate the variables and data points within the well-known iris flower data set associated with Ronald A Fisher

from ucimlrepo import fetch_ucirepo 

# fetch dataset 
iris = fetch_ucirepo(id=53)

# data (as pandas DataFrames) 
iris_ds_features = iris.data.features 
iris_ds_targets = iris.data.targets

# add the class column so all variables ar ein one DataFrame 
iris_ds_features['class'] = iris_ds_targets['class']
print(type(iris_ds_features))

# rename the DataFrame Columns - rename the existing DataFrame (rather than creating a copy) 
iris_ds_features.rename(columns={'sepal length': 'sepal_length_cm', 'sepal width': 'sepal_width_cm', 'petal length': 'petal_length_cm', 'petal width': 'petal_width_cm', 'class': 'species'},  inplace=True)

# remove the Iris- string from the species entries
iris_ds_features['species'] = iris_ds_features['species'].str.replace('Iris-', '')


print(iris_ds_features.isnull().sum())
# metadata 
# print(iris.metadata) 
# print(iris_ds_features)
# variable information 
print('\n')
print(iris.variables)