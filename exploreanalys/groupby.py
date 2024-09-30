import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
data = pd.read_csv('exploreanalys\\groupby.csv')
print(data.head())

print("Now we gonna group the table sales reveneue genreated by churned")
SRG_churned = data.groupby('churned')['Sales Revenue Generated'].mean()
print(SRG_churned)