# -*- coding: utf-8 -*-
"""
@author: pambh
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup



#print(States)
States = pd.read_csv("States-UT.csv")
# data = {'State':  ["gujarat",'goa']}
# States = pd.DataFrame(data)


months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
years = ["2015","2016","2017","2018","2019"]


#url = "https://weatherandclimate.com/gujarat/may-2019"
#url = "https://weatherandclimate.com/"+ States + "/" +months +"-2019"



data_frames = []


for index, States in States.iterrows(): #index,
    state = States['State']  # Assuming column name in CSV is 'State'
    for year in years:  
    
        for month in months:
        
        # Construct URL for each state and month
            url = f"https://weatherandclimate.com/{state.lower()}/{month}-{year}"
           
            # Fetch the webpage content
            #https://www.geeksforgeeks.org/response-url-python-requests/
            response = requests.get(url)
            #https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                
                # Fetch data from tb7 for each webpage
                table = soup.find("table", class_="tb7")
                
                if table:
                    # Convert HTML table to DataFrame
                    #Filtering Required Data
                    df = pd.read_html(str(table))[0]
                    df = df.drop(0)
                    df = df.drop("Dew Point", axis = 1)
                    df = df.drop("Time", axis =1)
                    df["Temperature"] = df["Temperature"].apply(lambda x: float(x.split('|')[0].strip()))
                    df["Humidity"] = df["Humidity"].astype(int)
                    df["Wind Speed"] = df["Wind Speed"].apply(lambda x: float(x.split('|')[0].strip()))
                    df["Pressure"] = df["Pressure"].apply(lambda x: float(x.split('|')[0].strip()))
                    df["Precipitation"] = df["Precipitation"].apply(lambda x: float(x.split('|')[0].strip()))
                   # print(df)
                    # Add columns for State and Month
    
                    #taking mean of each dailt data
                    AvgData = df.mean().to_frame().transpose()
                   
                    AvgData['State'] = state
                    AvgData['Month'] = month
                    AvgData['Year'] = year
                    #AvgData.set_index('Month' , inplace=True)
                    # Append DataFrame to list
                    #print(AvgData)
                    data_frames.append(AvgData)
                else:
                    print(f"No table found for {state} - {month} - {year}")
            else:
                print(f"Failed to fetch data for {state} - {month} - {year}")
            
# Concatenate all DataFrames into a single one
result_df = pd.concat(data_frames, ignore_index=True)
result_df.to_csv('raw tourism data/weather_data_2015-19.csv', index = False, mode='w+' )



