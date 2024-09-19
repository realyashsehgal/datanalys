import pandas as pd
import numpy as np
import sklearn.impute as SimpleIputer

data = pd.read_csv('locfilter.csv')
print(data.head(10))
print("Now filtering rows and columnsewy")
fltereddata = data.loc[0:9,'Age' : 'Height' ]
print(fltereddata)
print("The iloc work similar except all you have to to do is change the column name to the index of the column")
anotherfilterdata = data.iloc[0:9,0:2]
print(anotherfilterdata)