import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer

data1 = pd.read_csv('merge and concate/data1.csv')
# print(data1.head(10)) 
data2 = pd.read_csv('merge and concate/data2.csv')
# print("\n\n",data2.head())

joined_data = pd.merge(data1,data2,on='EmployeeID',how='inner')
print(joined_data)