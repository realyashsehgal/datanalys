import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer

data = pd.read_csv('isinfilter.csv')
print(data.head(10))

print("Now we filter the people who are emplyed in diffrent variable using isin")
filtered_prof = data[data['Profession'].isin(['Employed'])]
print(filtered_prof)