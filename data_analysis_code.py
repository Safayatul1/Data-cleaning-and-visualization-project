# Data Cleaning and Visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('data.csv')

# Fill missing values
calories_mode = data['Calories'].mode()[0]
data['Calories'].fillna(calories_mode, inplace=True)
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Drop duplicates
data.drop_duplicates(inplace=True)

# Handle outliers in Duration
data['Duration'] = np.where(data['Duration'] > 300, 300, data['Duration'])

# Visualize the data
# Scatter plot: Duration vs Calories
plt.figure(figsize=(8, 6))
plt.scatter(data['Duration'], data['Calories'], alpha=0.7, color='blue')
plt.xlabel('Duration (minutes)')
plt.ylabel('Calories Burned')
plt.title('Duration vs Calories')
plt.grid(True)
plt.show()

# Scatter plot: Pulse vs Calories
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Pulse', y='Calories', alpha=0.7, color='green')
plt.xlabel('Pulse')
plt.ylabel('Calories Burned')
plt.title('Pulse vs Calories')
plt.grid(True)
plt.show()

# Correlation heatmap
correlations = data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Line plot: Trends over time
plt.figure(figsize=(10, 6))
for column in ['Pulse', 'Maxpulse', 'Calories']:
    plt.plot(data['Date'], data[column], label=column)
plt.legend()
plt.title('Trends over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# Polynomial regression: Pulse vs Calories
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Prepare data for polynomial regression
X = data['Pulse'].values.reshape(-1, 1)
y = data['Calories']

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Fit the model
model = LinearRegression()
model.fit(X_poly, y)

# Predictions
y_pred = model.predict(X_poly)

# Visualize Polynomial Regression
plt.figure(figsize=(8, 6))
plt.scatter(data['Pulse'], data['Calories'], alpha=0.7, color='blue', label='Data Points')
plt.plot(data['Pulse'], y_pred, color='red', label='Polynomial Fit (degree=2)')
plt.title('Non-Linear Relationship (Pulse vs. Calories)')
plt.xlabel('Pulse')
plt.ylabel('Calories Burned')
plt.legend()
plt.grid(True)
plt.show()

# Print R^2 score
print(f'R^2 Score: {r2_score(y, y_pred):.2f}')
