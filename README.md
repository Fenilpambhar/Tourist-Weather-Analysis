# Final_Project
This is the final project for Data Science course. The main purpose of this project is to explore the relationship between weather and tourism in India, using data from 2015 to 2019. The main research question is: how do temperature, precipitation, humidity, wind speed, and rain influence the monthly tourist arrivals in various states of India? 

# Instructions
Required dependncy can be install by simply running the below command
```shell
pip install --user numpy pandas matplotlib scikit-learn
```
### Data gathering
1. Data has already been scrapped and cleaned as required for the analysis and store in cleand_data folder. You can directly perform the Stastical Analysis (3)
2. data_gathering_scripts folder have all the scripts in order gather data and combine data from different sources.
 > to scrap weather data and combine it with Rainfall data simply run
```shell
python3 1-weather_data.py
python3 2-weather_rain_combined.py
```
 > to filter the tourist data and combine it with weather data, run:
 ```shell
python3 3-tourists_data.py
python3 4-Combined_all_data.py
```
### Perform Analysis
3. The Analysis folder contains the script for the data analysis and prediction model which can be simply run by 
```shell
python3 5-analysis.py
python3 6-Prediction_model.py
```
Analysis script will produce some statistical output to help us conclude the behaviuor of data <br/>
Once Analysis is performed, Please take a look at Graphs folder for the output visulisation of the analysis. 

# Folder Structure
. <br />
├── raw tourism data  <br />
├   └── Contains raw data collected from credible sources <br />
├── docs <br />
├   └── contains Report of Analysis <br />
├── cleaned_data <br />
├   └── Contains output data from scrip 1-4/ Data used for analysis <br />
├── data_gathering_scripts <br />
├   └── Conatians script to scrap/combine/filter the data as required for analysis <br />
├── Analysis <br />
├   └── Conatins script to generate the plots and do anlysis <br />
├── Graphs <br/>
├   └── Contains plots from analysis scripts <br />
└── README.md <br />

# Note

•	The raw tourism data folder contains data downloaded from https://data.gov.in/search?title=monthly%20tourist%20in%20each%20state. <br />
• The Rainfall-data foldser have data for each state extracted from "Rainfall Statistics of India" 
•	The doc folder contains project analysis report. <br />
•	The cleaned_data folder contains output of the scripts used to clean the raw data which are in data_gathering_scripts folder <br />
•	The data_gathering_scripts folder contains scripts used to obtain the cleaned data. Which involves scraping of weatherandclimate.com website to obtain weather data.  <br />
•	The Alaysis folder contains scripts of the analysis. <br />


