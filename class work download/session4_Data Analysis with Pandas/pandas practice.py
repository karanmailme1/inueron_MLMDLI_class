# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 00:32:25 2021
@author: 17jan

pandas practice
"""

#part 1

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

#read above file
df = pd.read_csv(url, sep='\t')

df.shape
df.info()
df.head()
df.tail(7)

#Print the name of all the columns.
print(df.columns)

#How is the dataset indexed?
print(df.index)

#Which was the most ordered item? and How many items were ordered?
#df.value_counts('item_name')
df.groupby('item_name').sum().sort_values('quantity', ascending=False).head(1)

#What was the most ordered item in the choice_description column?
c = df.groupby('choice_description').sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)

#Turn the item price into a float
dollar = lambda x: float(x[1:])
df['item_price'] = df['item_price'].apply(dollar)
df

#How much was the revenue for the period in the dataset?
revenue = (df['quantity']* df['item_price']).sum()
print('Revenue was: $' + str(np.round(revenue,2)))

#print a data frame with only two columns item_name and item_price
df[['item_name','item_price']]

# delete the duplicates in item_name and quantity
filtered = df.drop_duplicates(['item_name', 'quantity'])
filtered

# select only the products with quantity equals to 1
one_prod = filtered[filtered.quantity == 1]
one_prod

# select only the item_name and item_price columns
price_per_item = one_prod[['item_name','item_price']]
price_per_item

# sort the values from the most to less expensive
price_per_item.sort_values(by='item_price',ascending=False)

#What was the quantity of the most expensive item ordered?
df.sort_values(by = "item_price", ascending = False).head(1)

#How many times were a Veggie Salad Bowl ordered?
df[df['item_name']=='Veggie Salad Bowl'].count()


###############################################


#Part 2

import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
df.shape
df.info()
df.head()

#Which continent drinks more beer on average?
df.groupby('continent')['beer_servings'].mean().sort_values(ascending=False).head(1)

#For each continent print the statistics for wine consumption.
df.groupby('continent')['wine_servings'].describe()


###############################################


#Part 3

import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)
crime.head()
crime.info()

#Convert the type of the column Year to datetime64
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')
crime.info()

#Set the Year column as the index of the dataframe
crime.set_index('Year', inplace=True)
crime.head(11)

#Group the year by decades and sum the values
#check offset alias: 
#https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
crimes = crime.resample('10AS').sum() #A=Year, S=Starting date of year
crimes
#or
#https://stackoverflow.com/questions/17764619/pandas-dataframe-group-year-index-by-decade
crime['Population'].groupby((crime.index.year//10)*10).sum()

# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10AS').max()
population
#or
crime['Population'].groupby(crime.index).max()

#update population column in df
crimes['Population'] = population
crimes

crime.head()

#Return the first 3 rows of the crime DataFrame df.
df = crime
df.iloc[:3]

#Select just the 'Murder' and 'Robbery' columns from the DataFrame df and print head
df[['Murder','Robbery']].head()

#select dataframe record by index and column name
#Select the data in rows [3, 4, 8] and in columns ['Murder', 'Robbery']
df.index[[3,4,8]]
df.loc[df.index[[3,4,8]],['Murder', 'Robbery']]

#Select only the rows where the number of murder is greater than 24,000
df[df['Murder'] > 24000]

#Select the rows the murder is between 20k and 24k (inclusive)
df[(df['Murder'] > 20000) & (df['Murder'] <= 24000)]
#or
df[df['Murder'].between(20000, 24000)]

#Calculate the mean murder for each different year in df.
df.groupby('Year')['Murder'].mean()
#or
df.groupby(df.index.year)['Murder'].mean()

#Sort df first by the values in the 'Murder' in decending order, 
#then by the value in the 'Violent' column in ascending order.
df.sort_values(by=['Murder','Violent'],ascending=[False,True])


###############################################


#Part 4

df = pd.read_csv('https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv')
df.info()
df.head()

#For each cyl type and each number of gears, find the mean mileage. 
df.groupby(['cyl','gear'])['mpg'].mean().reset_index()
#or
df.pivot_table(index='cyl', columns='gear', values='mpg', aggfunc='mean')
































