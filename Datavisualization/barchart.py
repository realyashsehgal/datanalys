import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Datavisualization\\barchart.csv')
freq_churned = data['churned'].value_counts()
plt.figure(figsize=(10,6))
freq_churned.plot(kind='bar')
plt.title("Frequency analysis of churned")
plt.xlabel('churned')
plt.ylabel('count')
plt.show()