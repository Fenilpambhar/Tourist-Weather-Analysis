import pandas as pd

percentage_share2019= pd.read_csv('raw tourism data/India-Tourism-Statistics-2020-TABLE_5.1.3.csv')
monthly_tourist_arrival2019=pd.read_csv('raw tourism data/India-Tourism-Statistics-2020-TABLE-2.3.1.csv')

percentage_share2018= pd.read_csv('raw tourism data/India-Tourism-Statistics-2019-Table-5.1.3.csv')

percentage_share2017= pd.read_csv('raw tourism data/Tourism_In_India_Statistics_2018-Table_5.1.3.csv')
monthly_tourist_arrival2017=pd.read_csv('raw tourism data/Tourism_In_India_Statistics_2018-Table_2.3.1.csv')

percentage_share2015_2016= pd.read_csv('raw tourism data/India-Tourism-Statistics-2015-2016-Table-5.1.3 -.csv')

monthly_tourist_arrival2015_2016=pd.read_csv('raw tourism data/India-Tourism-Statistics-2015-2016-Table-2.3.1.csv')


new={ 'State/UT' : percentage_share2019['States/UTs   *']}
df = pd.DataFrame(new)

Month= [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
    'December'
]

Visitors=pd.DataFrame({'Month': monthly_tourist_arrival2019['Months'] , 
                       '2019': monthly_tourist_arrival2019['2019'],
                       '2018': monthly_tourist_arrival2019['2018'],
                       '2017':  monthly_tourist_arrival2019['2017'],
                       '2016':  monthly_tourist_arrival2015_2016['Foreign Tourist Arrivals by Month - 2016'],
                       '2015':  monthly_tourist_arrival2015_2016['Foreign Tourist Arrivals by Month - 2015']
                       })

Foreign_percentage=pd.DataFrame({'State/UT' : percentage_share2019['States/UTs   *'], 
                                 'percentage2019' : percentage_share2019['PERCENTAGE SHARE - Foreign'], 
                                 'percentage2018' : percentage_share2018['Percentage Share - Foreign'],
                                 'percentage2017' : percentage_share2017['Percentage Share - Foreign'],
                                 'percentage2016' : percentage_share2015_2016['Percentage Share - Foreign 2016'],
                                 'percentage2015' : percentage_share2015_2016['Percentage Share - Foreign 2015']
                                 })



# Repeated each state 12 times for each month
df = df.loc[df.index.repeat(len(Month))]
df['Month'] = Month * len(new['State/UT'])
# Reset the index to get consecutive indices
df.reset_index(drop=True, inplace=True)

merged_df1 = pd.merge(df, Visitors, on='Month' )
merged_df=pd.merge(merged_df1, Foreign_percentage, on='State/UT')

merged_df['2019'] = merged_df['2019'].str.replace(',', '').astype(int)
merged_df['2018'] = merged_df['2018'].astype(int)
merged_df['2017'] = merged_df['2017'].astype(int)
merged_df['2016'] = merged_df['2016'].astype(int)
merged_df['2015'] = merged_df['2015'].astype(int)

merged_df['percentage2019'] = merged_df['percentage2019'].astype(float)
merged_df['percentage2018'] = merged_df['percentage2018'].astype(float)
merged_df['percentage2017'] = merged_df['percentage2017'].astype(float)
merged_df['percentage2016'] = merged_df['percentage2016'].astype(float)
merged_df['percentage2015'] = merged_df['percentage2015'].astype(float)

merged_df['Monthly_visitors2019'] = merged_df['2019'] * merged_df['percentage2019']/100
merged_df['Monthly_visitors2018'] = merged_df['2018'] * merged_df['percentage2018']/100
merged_df['Monthly_visitors2017'] = merged_df['2017'] * merged_df['percentage2017']/100
merged_df['Monthly_visitors2016'] = merged_df['2016'] * merged_df['percentage2016']/100
merged_df['Monthly_visitors2015'] = merged_df['2015'] * merged_df['percentage2015']/100

#Save
merged_df.to_csv('cleaned_data/Tourist.csv',index=False)


