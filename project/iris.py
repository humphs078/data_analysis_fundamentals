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

# metadata 
# print(iris.metadata) 
  
# variable information 
print('\n')
print(iris.variables)