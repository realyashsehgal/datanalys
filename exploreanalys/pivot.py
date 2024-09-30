import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
data = pd.read_csv('exploreanalys\\pivot.csv')
pivot_table = data.pivot_table(index = 'churned', 
                                         values = ['Task Completion Rates', 'Interpersonal Skills Rating'], 
                                         aggfunc = {'Task Completion Rates':'mean', 'Interpersonal Skills Rating':'mean', 'churned':'count'})
print(pivot_table)