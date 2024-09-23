import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
maindata = pd.read_csv('merge and concate/concmain.csv')
print(maindata.head())
print("Now we are going to concate our data")