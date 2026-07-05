import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#General Task 1: General Data Overview: 
#a. Check the first few rows of the dataset to understand its structure
MC = pd.read_csv('marketing_campaign.csv')
df = pd.DataFrame(MC)
#print(df.head())
#print(df.to_string())
print(df.info()) #b. Check the data types of each column 
print(df.isnull().sum()) #Check for any missing values in the dataset 
print(df.isnull().sum().sum()) #Total missing values

#Task 2: Descriptive Statistics: 
#a. Compute summary statistics for numerical columns (mean, median, min, max, and standard deviation)
print(df.describe())
#b. Explore the distribution of numerical variables using histograms or box plots 
plt.figure(figsize=(6,4))
plt.boxplot(df["Income"].dropna())
plt.title("Boxplot of Income")
plt.show() #Distribution of Customer Income using Boxplot
df[["NumWebPurchases","NumStorePurchases","NumCatalogPurchases","NumDealsPurchases"]].hist(figsize=(12,6),bins=5)
plt.tight_layout()
plt.show() #Distribution of Customer by No. of Web and Store Purchases by Histogram

#Task 3: Univariate Analysis: ("What can I learn from this single column?")
#a. Explore the distribution of each numerical variable using histograms or kernel density plots
plt.figure(figsize=(12,6))
plt.hist(df["Income"].dropna(),bins=20)
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.title("Distribution of Customer Income")
plt.show() #Distribution of Customer Income using Histogram
Yr2012 = df[df["Year"]==2012] #//Optional
print(Yr2012)
df1 = df.groupby('Month')['Recency'].mean()
df1.plot(x='Month',y='Recency',kind='bar')
plt.show() #Distribution of Recency using bar chart

#b. Explore the distribution of each categorical variable using bar plots or pie charts
df.groupby('Education')[['Response']].sum().sort_values('Response').plot(kind='bar')
plt.title('Response received by Education')
plt.show() #Response received by Education

df2=df.groupby('Education')[['Income']].mean().sort_values('Income')
df2['Income'].plot(kind='pie',autopct='%1.1f%%',figsize=(8,8))
plt.title('Average Income by Education')
plt.show() #Average Income by Education

#Task 4: Bivariate Analysis: 
#Explore the relationship between categorical variables and the target variable using bar plots
pd.crosstab(df['Education'], df['Response']).plot(    kind='bar',    figsize=(8,5))
plt.title('Response by Education')
plt.xlabel('Education')
plt.ylabel('Customer Count')
plt.show()

#c. Explore the relationship between numerical and categorical variables using box plots 
df.boxplot(column='Recency', by='Response')
plt.title('Recency by Response')
plt.suptitle('')
plt.show()
