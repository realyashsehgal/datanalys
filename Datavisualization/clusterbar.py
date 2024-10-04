import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Datavisualization\\clusteredbar.csv')
cross_tab = pd.crosstab(data['churned'], data['Accuracy of Work'])
plt.figure(figsize=(8, 6))
cross_tab.plot(kind='bar',stacked=False)
plt.title('Working accuracy level by churned employees')
plt.xlabel('Churned')
plt.ylabel('Count')
plt.show()