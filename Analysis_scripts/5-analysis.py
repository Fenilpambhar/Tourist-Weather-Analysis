# -*- coding: utf-8 -*-
"""
@author: pambh
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.nonparametric.smoothers_lowess import lowess
from statsmodels.stats.multicomp import pairwise_tukeyhsd



data = pd.read_csv("cleaned_data/Complete_merged_data.csv")

## Finding correlation with Visitors

print(data[["Temperature","Visitors"]].corr()) 

top_ten = ["tamil-nadu", "uttar-pradesh","delhi","goa","kerala","rajasthan","maharashtra", "punjab", "west-bengal","bihar"]
top_ten_df = data[data["State"].isin(top_ten)]
#top_ten_df.to_csv("top_ten_state_data.csv", index= False, mode="w+")
correlation_matrices = top_ten_df.groupby('State').apply(lambda x: x[['Visitors', 'Temperature']].corr())

color_palette = sns.color_palette("tab10", len(top_ten_df['State'].unique()) )

## all State to visualise the spread od data

plt.figure(figsize=(18, 10))
plt.xticks(rotation=50)
sns.scatterplot(data=data, x='Temperature', y='Visitors', hue='State', palette=color_palette)
plt.plot()
plt.title('Monthly Foreign Visitors trend in India')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(False)
plt.savefig('Graphs/All_State_vs Visitors.png', bbox_inches='tight')  # Save the plot before displaying
#plt.show()




## Narrow down to top 10 most visitied state

##### Temperature vs visitors
plt.figure(figsize=(10, 8))
sns.scatterplot(data= top_ten_df, x='Temperature', y='Visitors', hue='State', palette=color_palette )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Scatter plot between Temperature Variables and number of Visitors')
#plt.tight_layout()  # Adjusts the plot to avoid overlapping elements
plt.grid(True)
plt.savefig('Graphs/temperature_vs_visitors.png', bbox_inches='tight') 
plt.show()


months_map = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 
              'july': 7,'august': 8, 'september':9,'october':10, 'november':11,'december':12} 
top_ten_df['Month_num'] = top_ten_df['Month'].map(months_map)
# Fiited line to see the trend
smoothed = lowess(top_ten_df['Temperature'], top_ten_df['Month_num']-1, frac=0.5)  # Adjust frac as needed


#### Temperature Trend
plt.figure(figsize=(10, 8))
plt.xticks(rotation=25)
sns.scatterplot(data=top_ten_df, x='Month', y='Temperature', hue='State', palette=color_palette)
plt.plot(smoothed[:, 0], smoothed[:, 1],  'r-', linewidth=3, label='LOESS fit')
plt.plot()
plt.title('Temperature over 5 year by month in India')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.savefig('Graphs/Temperature_trend.png', bbox_inches='tight')  # Save the plot before displaying
#plt.show()


####Visitors
smoothed = lowess(top_ten_df['Visitors'], top_ten_df['Month_num']-1, frac=0.4)  

plt.figure(figsize=(10, 8))
plt.xticks(rotation=25)
sns.scatterplot(data=top_ten_df, x='Month', y='Visitors', hue='State', palette=color_palette)
plt.plot(smoothed[:, 0], smoothed[:, 1],  'r-', linewidth=3, label='LOESS fit')

plt.plot()
plt.title('Monthly Foreign Visitors trend in India')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.savefig('Graphs/Visitors_trend.png', bbox_inches='tight')  # Save the plot before displaying
#plt.show()

#### state vs visitors

plt.figure(figsize=(10, 8))
plt.xticks(rotation=25)
sns.scatterplot(data=top_ten_df, x='State', y='Visitors', hue='Year', palette=color_palette)
#plt.plot(smoothed[:, 0], smoothed[:, 1],  'r-', linewidth=3, label='LOESS fit')
#sns.regplot(data=top_ten_df, x='Month_num', y='Temperature', scatter=False) 
plt.plot()
plt.title('Monthly Foreign Visitors trend in India')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.savefig('Graphs/State_vs Visitors.png', bbox_inches='tight')  # Save the plot before displaying
#plt.show()


posthoc = pairwise_tukeyhsd(
    top_ten_df['Temperature'], top_ten_df['State'],
    alpha=0.05)
print(posthoc)
fig = posthoc.plot_simultaneous()