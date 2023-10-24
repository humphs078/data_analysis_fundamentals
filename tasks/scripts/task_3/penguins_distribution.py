# penguins_distribution.py
# Author: Sean Humphreys
# Solution to Task 3 on the Fundamentals of Data Analysis module 2023. Task - "give an overview
# of the famous penguins data set,2 explaining the types of variables it contains. Suggest the
# types of variables that should be used to model them in Python, explaining your rationale.""

# ref - https://medium.com/@marvelouskgc/build-a-penguin-project-using-pandas-and-seaborn-eugene-tsai-e4b7e0b499ea

# import the pandas module used to read in the data set file as a data frame
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
print(penguins)

penguins_summary = penguins.describe()

flip = penguins.loc[penguins['species'] =='Adelie']['flipper_length_mm'].dropna().reset_index(drop=True)
print(flip)

fig, axs = plt.subplots()
axs.hist(flip, bins=30)
plt.show()