import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
data = pd.read_csv('exploreanalys\\descriptive.csv')
print(data.head())
print(round(data.describe()))