import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer

data = pd.read_csv('exploreanalys/freqandperc.csv')
print(data.head())
short_data = data[['EmployeeID', 'gender', 'churned']]
print(short_data)
freq_chruned = data['churned'].value_counts()
print(freq_chruned)
perc_chruned = freq_chruned/len(data['churned'])*100
print(round(perc_chruned,2))