import numpy as np
import matplotlib.pyplot as plt
# mu, sigma = 0, 0.1 # mean and standard deviation

# s = np.random.normal(mu, sigma, 1000)
# print(s)
# plt.hist(x=s)
# plt.show()

# import the required software libraries
import pandas as pd
import seaborn as sns
penguins = sns.load_dataset('penguins')

summary = penguins.describe()
print(summary)
x = summary.loc['mean', 'bill_length_mm']
print(x)
print(type(x))
print(penguins)
# penguins = penguins.fillna(penguins.median())
penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']] = penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].fillna(penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].median())
print(penguins)