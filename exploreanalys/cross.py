import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
data = pd.read_csv('exploreanalys\\cross.csv')
cross_tab = pd.crosstab(data['churned'],data['Accuracy of Work'])
print(cross_tab)