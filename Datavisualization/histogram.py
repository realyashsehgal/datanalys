import pandas as pd 
import numpy as np
import sklearn.impute as SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns 
data = pd.read_csv('Datavisualization\\histogram.csv')
plt.figure(figsize=(8, 6))
data['Task Completion Rates'].plot(kind='hist',bins=4)

plt.title('Histogram of Task Completion Rates')
plt.xlabel('Task Completion Rates')
plt.ylabel('Frequency')
plt.show()