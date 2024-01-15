# -*- coding: utf-8 -*-
"""
@author: pambh
"""
import pandas as pd


years = ["2015","2016","2017","2018","2019"] 
weather_data = pd.read_csv("raw tourism data/weather_data_2015-19.csv")
combined = []
for year in years:
    Rainfall_data = pd.read_csv("Rainfall-data/Rainfall-stats-"+year+".csv")


    Rainfall_data =Rainfall_data.melt(id_vars = ['STATES'])
    weather_data_by_year = weather_data[weather_data["Year"].astype(str) == year]
    #print(weather_data_by_year)
    #print(Rainfall_data, weather_data)
    # Convert 'Month' column to title case for consistency
    # weather_data['Month'] = weather_data['Month'].str.title()
    # if (weather_data["Year"] == year):
    # # Merge the two DataFrames on 'STATES' and 'Month'
    merged_df = pd.merge(weather_data_by_year, Rainfall_data, left_on=['State','Month'], right_on=['STATES','variable'])
    
    merged_df = merged_df.drop(['STATES','variable'], axis = 1)
    merged_df = merged_df[merged_df['State'] != 'ladakh']                
    merged_df = merged_df.rename(columns = {'value' : "RainFall"})
    combined.append(merged_df)
# # Drop the duplicate 'Month' column
# merged_df.drop('Month', axis=1, inplace=True)

# # Display the merged DataFrame

result_df = pd.concat(combined, ignore_index=True)
result_df.to_csv('cleaned_data/weather_data.csv', index = False, mode='w+' )