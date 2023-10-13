# iris.py
# Author: Sean Humphreys
# Script to investigate the variables and data points within the well-known iris flower data set associated with Ronald A Fisher

from ucimlrepo import fetch_ucirepo 

# fetch dataset 
iris = fetch_ucirepo(id=53)

# data (as pandas dataframes) 
iris_ds_features = iris.data.features 
iris_ds_targets = iris.data.targets


iris_ds_features['class'] = iris_ds_targets['class']
print(type(iris_ds_features))

# rename the DataFrame Columns
# Or rename the existing DataFrame (rather than creating a copy) 
iris_ds_features.rename(columns={'sepal length': 'sepal_length_cm', 'sepal width': 'sepal_width_cm', 'petal length': 'petal_length_cm', 'petal width': 'petal_width_cm', 'class': 'species'},  inplace=True)

iris_ds_features['species'] = iris_ds_features['species'].str.replace('Iris-', '')

print(iris_ds_features(head))

# metadata 
# print(iris.metadata) 
print(iris_ds_features)
# variable information 
print('\n')
# print(iris.variables)