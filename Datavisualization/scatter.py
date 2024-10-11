import pandas as pd
import matplotlib.pyplot as plt

final_data = pd.read_csv("Datavisualization\\scatter.csv", header=0)

plt.figure(figsize=(8, 6))
plt.scatter(final_data['Interpersonal Skills Rating'],final_data['Decision-Making Skills Rating'])

plt.title('Scatterplot of Interpersonal Skills Rating vs Decision-Making Skills Rating')
plt.xlabel('Interpersonal Skills Rating')
plt.ylabel('Decision-Making Skills Rating')
plt.show()