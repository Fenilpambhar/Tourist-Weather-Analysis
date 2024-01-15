# -*- coding: utf-8 -*-
"""
@author: pambh
"""
import pandas as pd

weather_data = pd.read_csv("cleaned_data/weather_data.csv")
#print(weather_data)


States = pd.read_csv("cleaned_data/States-dictonary.csv")
value_mapping = dict(zip(States['State/UT'], States['State']))


tourist = pd.read_csv("cleaned_data/Tourist.csv")

tourist["State/UT"] = tourist["State/UT"].map(value_mapping)
tourist = tourist.rename(columns = {'State/UT' : "State"})
tourist["Month"] = tourist["Month"].str.lower()


#print(tourist)

#tourist.to_csv("Tourist_data.csv",  index = False, mode='w+' )




years = ["2015","2016","2017","2018","2019"] 
merged = []
for year in years:
    weather_2015 = weather_data[weather_data["Year"].astype(str) == year]
    tourist_2015 = tourist[["State", "Month", "Monthly_visitors"+year]]
    
    
    merger = pd.merge(weather_2015, tourist_2015, on=["State", "Month"] )
    merger = merger.rename(columns = {"Monthly_visitors"+year : "Visitors"})
    merged.append(merger)
    
matrix = ["Temperature", "Humidity", "Wind Speed", "Pressure", "Precipitation", "RainFall", "Visitors"]
    
correlation_matrix = merger[matrix].corr()
    # print(correl)
merged = pd.concat(merged, ignore_index=True)  
merged.to_csv("cleaned_data/Complete_merged_data.csv", index= False, mode="w+")
