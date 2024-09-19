import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
data = pd.read_csv('queryfilter.csv')
print(data.head(10))

print("We are going to filter the data based on height more than 180")

height_data = data.query('Height > 180')
print(height_data)