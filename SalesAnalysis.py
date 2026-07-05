#1. Prepare Data for Analysis:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sales = pd.read_csv('Sales.csv') #read csv file
df = pd.DataFrame(sales) #create dataframe from csv file
#print(df.to_string())
#print(df.info()) #check data types and missing values
#print(df.describe()) #check summary statistics
#print(df.shape) #check number of rows and columns
#print(df.isnull().sum()) #check for missing values
#print(df.notnull().sum()) #check for non-missing values
#print(df.dtypes) #check data types of all columns to ensure 'Date' is in datetime format
df['Date'] = pd.to_datetime(df['Date'],dayfirst=True) #convert 'Date' column to datetime format (Date was in str format.Hence, we're not getting line chart in sorted order. We need to convert it to datetime format for analysis. 
#print(df) #set 'Date' column as index for easier time-based analysis (This will allow us to easily group and analyze data based on dates. It also makes it easier to plot time series data, as the date will be on the x-axis.)
#The dayfirst=True parameter is used to specify that the day comes before the month in the date format.)
#print(df.dtypes) #check data types again to confirm 'Date' is now in datetime format

#2.Normalize data for analysis:
#df_dataonly = pd.DataFrame(df)
df_dataonly = df.select_dtypes(include="number") #select only numeric columns for analysis(Filtered DF by using select_dtypes() method to include only numeric columns)
#print(df_dataonly)
normalized_df = (df_dataonly - df_dataonly.min()) / (df_dataonly.max() - df_dataonly.min()) #normalize data using min-max scaling
#print(normalized_df)
#print(f'Minimum value of normalized data: \n{normalized_df.min()}') #check minimum of normalized data(shows min of both the columns)
#print(f'Maximum value of normalized data: \n{normalized_df.max()}') #check maximum of normalized data(shows max of both the columns)

#print(f'Minimum value of normalized data: {normalized_df.min().min()}') #check minimum of normalized data(shows min of entire dataframe)
#print(f'Maximum value of normalized data: {normalized_df.max().max()}') #check maximum of normalized data(shows max of entire dataframe)
#.min().min() it'll find minimum value of each column and then find minimum of those minimum values, giving us the overall minimum value in the entire dataframe. 
# Similarly, .max().max() will find maximum value of each column and then find maximum of those maximum values, giving us the overall maximum value in the entire dataframe.

#3. Visualize Overall Trends:
#Line_Charts = df.groupby('Date')[['Sales']].sum().sort_values(by='Date', ascending=True).plot(kind='line', marker='o', linestyle='-', color='b') #line chart for sales over time
#plt.title('Sales Over Time') #title for the line chart
#plt.xlabel('Date') #label for x-axis
#plt.ylabel('Sales') #label for y-axis

#fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,6)) #create a figure with 1 row and 2 columns of subplots
#ax1.plot(df.groupby('Date')[['Sales']].sum().sort_values(by='Date', ascending=True), marker='o', linestyle='-', color='r') #line chart for sales over time
#ax2.plot(df.groupby('Date')[['Unit']].sum().sort_values(by='Date', ascending=True), marker='o', linestyle='-', color='g') #line chart for unit over time
#ax1.set_title('Sales Over Time') #title for the line chart
#ax2.set_title('Units Over Time') #title for the line chart
#ax1.set_xlabel('Date') #label for x-axis
#ax2.set_xlabel('Date') #label for x-axis
#ax1.set_ylabel('Sales') #label for y-axis
#ax2.set_ylabel('Units') #label for y-axis
#plt.show() #display the line chart

#4. Analyze Monthly Data:
df.set_index('Date', inplace=True) #set 'Date' column as index for easier time-based analysis (This will allow us to easily group and analyze data based on dates. It also makes it easier to plot time series data, as the date will be on the x-axis.)
oct_data = df.loc['2020-10-01':'2020-10-31'] #filter data for October 2020 using .loc[] method to select rows based on date range. This will give us a new dataframe containing only the data for October 2020. We can then analyze this subset of data to understand the sales and units trends specifically for that month.
#print(oct_data) #print the filtered data for October 2020 to verify that we have the correct subset of data for analysis
nov_data = df.loc['2020-11-01':'2020-11-30'] #filter data for November 2020 using .loc[] method to select rows based on date range. This will give us a new dataframe containing only the data for November 2020. We can then analyze this subset of data to understand the sales and units trends specifically for that month.
dec_data = df.loc['2020-12-01':'2020-12-31'] #filter data for December 2020 using .loc[] method to select rows based on date range. This will give us a new dataframe containing only the data for December 2020. We can then analyze this subset of data to understand the sales and units trends specifically for that month.

#Analysis:
#for i,j in zip(['October','November','December'],[oct_data,nov_data,dec_data]):
    #print(f'{i} 2020 Sales: {j['Sales'].sum()}') #calculate total sales for each month by summing the 'Sales' column in each monthly dataframe
    #print(f'{i} 2020 Units: {j['Unit'].sum()}') #calculate total units for each month by summing the 'Unit' column in each monthly dataframe
    #print(f'{i} 2020 Average Sales: {j['Sales'].mean()}') #calculate average sales for each month by taking the mean of the 'Sales' column in each monthly dataframe
    
#5. Describe Data:
#print(f'Analysis of Entire Dataset: {df.describe()}\n')
#print(f'October 2020: {oct_data.describe()}\n')
#print(f'November 2020: {nov_data.describe()}\n')
#print(f'Dcember 2020: {dec_data.describe()}')

#6. Analyze Unit Data:
#Unit Analysis(Boxplot):
#fig = plt.figure(figsize=(12,6)) #create a figure with specified size
#ax = fig.add_axes([0.1,0.1,0.8,0.8]) #add axes to the figure with specified position and size
#ax.boxplot([oct_data['Unit'], nov_data['Unit'], dec_data['Unit']], labels=['October', 'November', 'December']) #create box plot for unit data of each month with specified labels
#ax.set_title('Unit Distribution by Month') #title for the box plot
#plt.show()
    
#Sales Analysis(Boxplot):
#fig = plt.figure(figsize=(12,6)) #create a figure with specified size
#ax = fig.add_axes([0.1,0.1,0.8,0.8]) #add axes to the figure with specified position and size
#ax.boxplot([oct_data['Sales'], nov_data['Sales'], dec_data['Sales']], labels=['October', 'November', 'December']) #create box plot for unit data of each month with specified labels
#ax.set_title('Sales Distribution by Month') #title for the box plot
#plt.show()
    
#7. Explore Monthly Plots and Analysis:
#Consolidated 3-month sales plot:
fig = plt.figure(figsize=(12,6)) #create a figure with specified size
ax = fig.add_axes([0.1,0.1,0.8,0.8])
df_all = pd.concat([oct_data, nov_data, dec_data]) #concatenate the three monthly dataframes into a single dataframe for easier plotting and analysis
df_all = df_all.groupby('Date')[['Sales']].sum().reset_index() #group the concatenated dataframe by 'Date' and sum the 'Sales' for each date to get the total sales for each date across all three months
df_all = df_all.sort_values(by='Date', ascending=True) #sort the grouped dataframe by 'Date' in ascending order to ensure that the line chart will be plotted in chronological order
ax = df_all.plot(x='Date',y='Sales', marker='o', linestyle='-', color='m', ax=ax) #plot the line chart for total sales over time using the grouped dataframe
#print(df_all) #print the grouped dataframe to verify that we have the correct total sales for each date
plt.xticks(rotation=45) #rotate x-axis labels for better readability
ax.set_title('Quarterly Sales Trend')
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
#plt.tight_layout()
#plt.show()

#Overall Unit and Sales figures:
Overall_Units = df['Unit'].sum() #calculate total units sold across the entire dataset by summing the 'Unit' column in the original dataframe
Overall_Sales = df['Sales'].sum() #calculate total sales across the entire dataset by summing the 'Sales' column in the original dataframe
#print(f'Overall Units Sold: {Overall_Units}') #print the total units sold   
#print(f'Overall Sales: {Overall_Sales}') #print the total sales

#Units sold in October, November, and December:
Oct_Units = oct_data['Unit'].sum() #calculate total units sold in October by summing the 'Unit' column in the October dataframe
Nov_Units = nov_data['Unit'].sum() #calculate total units sold in November by summing the 'Unit' column in the November dataframe
Dec_Units = dec_data['Unit'].sum() #calculate total units sold in December by summing the 'Unit' column in the December dataframe
print(f'Units Sold in October 2020: {Oct_Units}\n') #print total  units sold in October
print(f'Units Sold in November 2020: {Nov_Units}\n') #print total units sold in November
print(f'Units Sold in December 2020: {Dec_Units}\n') #print total units sold in December

#Sales numbers for October, November, and December:
Oct_Sales = oct_data['Sales'].sum() #calculate total sales in October by summing the 'Sales' column in the October dataframe
Nov_Sales = nov_data['Sales'].sum() #calculate total sales in November by summing the 'Sales' column in the November dataframe
Dec_Sales = dec_data['Sales'].sum() #calculate total sales in December by summing the 'Sales' column in the December dataframe
print(f'Sales in October 2020: {Oct_Sales}\n') #print total  sales in October
print(f'Sales in November 2020: {Nov_Sales}\n') #print total sales in November
print(f'Sales in December 2020: {Dec_Sales}\n') #print total sales in December

#9. Analyze Statewise Sales in the United States:
Sateswise_Sales = df.groupby('State')[['Sales']].sum().sort_values(by='State', ascending=True) #group the original dataframe by 'State' and sum the 'Sales' for each state to get total sales for each state, then sort the resulting dataframe by 'Sales' in descending order to see which states have the highest sales
print(f'Statewise Sales in the United States: \n{Sateswise_Sales}\n') #print the statewise sales dataframe to see the total sales for each state in the United States, sorted from highest to lowest sales

#10. Conduct Groupwise Analysis:
Groupwise_Sales = df.groupby('Group')[['Sales']].sum().sort_values(by='Group', ascending=True) #group the original dataframe by 'Group' and sum the 'Sales' for each group to get total sales for each group, then sort the resulting dataframe by 'Sales' in descending order to see which groups have the highest sales
print(f'Groupwise Sales: \n{Groupwise_Sales}\n')

#11. Explore Timewise Analysis:
Timewise_Sales = df.groupby('Time')[['Sales']].sum().sort_values(by='Time', ascending=True) #group the original dataframe by 'Time' and sum the 'Sales' for each time period to get total sales for each period, then sort the resulting dataframe by 'Time' in ascending order
print(f'Timewise Sales: \n{Timewise_Sales}\n')

#8. Obtain a Comprehensive Snapshot:
print(f'Total Sales: {Overall_Sales}\n') #print total sales across the entire dataset
print(f'Total Units Sold: {Overall_Units}\n') #print total units sold across the entire dataset
print(f'Average Sales: {df['Sales'].mean()}\n') #calculate and print average sales across the entire dataset by taking the mean of the 'Sales' column in the original dataframe

#Best & Worst Month:
Monthly_Sales = {'October': Oct_Sales,
                 'November': Nov_Sales,
                 'December': Dec_Sales} #create a dictionary to store total sales for each month
#print(Monthly_Sales)

Best_Month = max(Monthly_Sales, key=Monthly_Sales.get) #Here max() finds oyt the maximum value by using keys in the dictionary hence, we're using key=Monthly_Sales.get which will 
#take each key (month) and return its corresponding value (total sales) from the Monthly_Sales dictionary, allowing max() to compare the total sales for each month and determine which month has the highest sales.
Worst_Month = min(Monthly_Sales, key=Monthly_Sales.get)
print(f'Best Month: {Best_Month}')
print(f'Worst Month: {Worst_Month}')
#find the month with the lowest sales by using the min() function on the Monthly_Sales dictionary, specifying that we want to compare values (total sales) to determine the minimum

