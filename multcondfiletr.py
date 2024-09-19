import pandas as pd
import numpy as np 
import sklearn.impute as SimpleImputer
data = pd.read_csv('multcondfilter.csv')
print(data.head(10))
print("Lets filter tha data with some conditions heheh")
filtered_data = data[(data['Weight'] > 50 ) & (data['Weight']<100)]
print(filtered_data)