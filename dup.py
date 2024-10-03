import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = pd.read_csv('dup.csv')
# print(data)
# print("Here in this code we will remove all the duplicate values ")
print(data.dtypes)
missing_col = []
for column in data:
    if data[column].dtype == np.int64 or np.float64 and data[column].isnull().any():
        missing_col.append(column)
        print("hell")
        print(data[column])
print(missing_col)
for col in data:
    imputer = SimpleImputer(strategy='mean')
    imputer.fit(data[[col]])
    data[[col]] = imputer.transform(data[[col]])
    
    
print(data.head(10))
# duplicate = data.duplicated()
# print(duplicate)
# print("We can also filter and check which is duplicate\n\n\n")
# print(data[duplicate])
# print("Now we drop the duplicated values from the data\n\n\n")
# data.drop_duplicates(inplace=True)#Here inplace true will make the changes in the real data
# data.to_csv('dup.csv', index=False)
# print("Changes have been saved permanently to 'dup.csv'.")
# print(data)