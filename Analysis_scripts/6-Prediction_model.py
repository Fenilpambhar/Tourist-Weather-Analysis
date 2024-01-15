# -*- coding: utf-8 -*-
"""
@author: pambh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from scipy import stats
import seaborn as sns
sns.set()

data = pd.read_csv("Complete_merged_data.csv")

#Taking Top 3 most visited states based on previous analysis to further predict

top_three_visited = ["maharashtra", "tamil-nadu","uttar-pradesh" ]

top_three_df = data[data["State"].isin(top_three_visited)]


####ANOVA
Visitors_1 = data[data["State"] == 'maharashtra']
Visitors_2 = data[data["State"] == 'tamil-nadu']
Visitors_3 = data[data["State"] == 'uttar-pradesh']
anova = stats.f_oneway(Visitors_1['Temperature'], Visitors_2['Temperature'], Visitors_3['Temperature'])
print("Anova:",anova)
print("P-values: ", anova.pvalue)


### Plot to visualize the trend
color_palette = sns.color_palette("tab10", len(top_three_df['Year'].unique()) )

plt.figure(figsize=(12, 10))
plt.xticks(rotation=50)
sns.scatterplot(data=top_three_df, x='Temperature', y='Visitors', hue='Year',  palette=color_palette )#, hue='State', palette=color_palette)
#plt.plot(smoothed[:, 0], smoothed[:, 1],  'r-', linewidth=3, label='LOESS fit')
#sns.regplot(data=top_ten_df, x='Month_num', y='Temperature', scatter=False) 
plt.plot()
plt.title('Monthly Foreign Visitors trend in India')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(False)
plt.savefig('Graphs/All_State_vs Visitors.png', bbox_inches='tight')  # Save the plot before displaying
#plt.show()


#### Sample Data for prediction model
temperature = top_three_df["Temperature"].values.reshape(-1, 1)
visitors = top_three_df["Visitors"].values.reshape(-1, 1)



# Fit polynomial regression model
poly = PolynomialFeatures(degree=4)  # You can change the degree of the polynomial
X_poly = poly.fit_transform(temperature)
model = LinearRegression()
model.fit(X_poly, visitors)

# Predict visitors based on the model
y_pred = model.predict(X_poly)

# Calculate R-squared and RMSE
r2 = r2_score(visitors, y_pred)
rmse = np.sqrt(mean_squared_error(visitors, y_pred))

print(f"R-squared: {r2}")
print(f"RMSE: {rmse}")

# Plotting the results
plt.figure(figsize=(10, 8))
plt.scatter(temperature, visitors, color='blue', label='Actual data', alpha=0.8)
plt.scatter(temperature, y_pred, color='red', label='Predicted data', linewidths=0.2)
plt.xlabel('Temperature')
plt.ylabel('Number of Visitors')
plt.title("Prediction of top three state's visitors")
plt.legend()
plt.savefig("Graphs/Prediction.png")
#plt.show()

# R-squared: 0.30406456939940596
# RMSE: 33814.17432471061