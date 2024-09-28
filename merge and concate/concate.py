import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
maindata = pd.read_csv('merge and concate/concmain.csv')
print(maindata.head())
print("Now we are going to concate our data with some more values\n\n")

new_data = pd.read_csv('merge and concate/conc1.csv')

concated_data = pd.concat([maindata,new_data]).reset_index()
print(concated_data.tail())
print( concated_data.dtypes)