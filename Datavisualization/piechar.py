import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Datavisualization\\piechart.csv')

freq_churned = data['churned'].value_counts()
perc_churned = freq_churned/len(data['churned'])*100
plt.figure(figsize=(8, 6))
perc_churned.plot(kind='pie',autopct='%1.2f%%')
plt.title('Percentage of churned employees')
plt.ylabel('')
plt.show()