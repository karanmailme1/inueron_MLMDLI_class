import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth', None)

# Part 1

df = pd.read_csv('https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv')
df.head(2)
df.shape
df1 = pd.read_csv('https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv')
df1.head(2)
df1.shape

#1. Get the Metadata from the above files.
df.info()
df1.info()

#2. Get the row names from the above files.
df.index.to_numpy()
df1.index.to_numpy()
#or
df.index.values

#3. Change the column name from any of the above file.
#4. Change the column name from any of the above file and store the changes made permanently
#https://datascienceparichay.com/article/pandas-rename-column-names/#:~:text=How%20to%20rename%20columns%20in%20pandas%3F%201%20Use,attribute%20to%20your%20new%20list%20of%20column%20names.
df.rename(columns={"Indicator":"Indicator_Id"}, inplace=True)
df.columns

#5. Change the names of multiple columns.
df.rename(columns={'PUBLISH STATES':'Publication Status', 'WHO region':'WHO Region'}, inplace=True)
df.columns

#6. Arrange values of a particular column in ascending order.
df.head()
df.sort_values(by='Year',axis=0).head()

#7. Arrange multiple column values in ascending order.
df.head()
df.sort_values(by=['Indicator_Id','Country','Year','WHO Region','Publication Status']).head()

#8. Make country​ as the first column of the dataframe.
#https://www.datasciencemadesimple.com/re-arrange-or-re-order-the-column-of-dataframe-in-pandas-python-2/#:~:text=1%20First%20Get%20the%20list%20of%20column%20names,the%20column%20by%20passing%20the%20sorted%20column%20names
df.columns
df = df[['Country', 'Indicator_Id', 'Publication Status', 'Year', 'WHO Region', 
         'World Bank income group', 'Sex', 'Display Value', 'Numeric', 'Low', 
         'High', 'Comments']]
df.columns

#9. Get the column array using a variable
df['WHO Region'].to_numpy()
#or
np.array(df[['WHO Region']])

#10. Get the subset rows 11, 24, 37
df.iloc[[11,24,37],:] #or df.iloc[[11,24,37]]

#11. Get the subset rows excluding 5, 12, 23, and 56
#https://stackoverflow.com/questions/63532746/how-to-get-a-subset-of-rows-in-a-dataframe-excluding-a-few-rows-python-pandas
df.drop([5,12,23,56], axis=0).shape


##############################################################


# Part 2

users = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv')
sessions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv')
products = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv')
transactions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv')

users.info()
sessions.info()
products.info()
transactions.info()

users.head()
sessions.head()
products.head()
transactions.head()

#12. Join users to transactions, keeping all rows from transactions and 
#only matching rows from users (left join)
pd.merge(transactions, users, how="left") #best
#or
transactions.join(users, lsuffix='_left', on='UserID', how='left')
#or
transactions.join(users.set_index('UserID'), on='UserID', how='left') #easiest
#or
transactions.set_index('UserID').join(users.set_index('UserID'), how='left').reset_index()

#13. Which transactions have a UserID not in users?
transactions[~transactions['UserID'].isin(users['UserID'])]

#14. Join users to transactions, keeping only rows from transactions and 
#users that match via UserID (inner join)
pd.merge(transactions, users, how='inner')

#15. Join users to transactions, displaying all matching rows AND 
#all non-matching rows (full outer join)
pd.merge(transactions, users, how='outer')

#16. Determine which sessions occurred on the same day each user registered
sessions
users
pd.merge(users, sessions, how='inner', left_on=['UserID','Registered'], right_on=['UserID','SessionDate'])

#17. Build a dataset with every possible (UserID, ProductID) pair (cross join)
#https://www.geeksforgeeks.org/python-program-to-perform-cross-join-in-pandas/
users_UserID = pd.DataFrame(users['UserID'])
products_ProductID = pd.DataFrame(products['ProductID'])
users_UserID['tempID'] = 1
products_ProductID['tempID'] = 1
users_UserID
products_ProductID
user_prod = pd.merge(users_UserID,products_ProductID,how='outer',on='tempID').drop(columns='tempID')
user_prod

#18. Determine how much quantity of each product was purchased by each user
user_prod_quant = pd.merge(user_prod,transactions,on=['UserID','ProductID'],how='left')
user_prod_quant.drop(columns=['TransactionID','TransactionDate'], inplace=True)
user_prod_quant['Quantity'].fillna(0,inplace=True)
user_prod_quant.groupby(['UserID','ProductID']).sum().reset_index()

#19. For each user, get each possible pair of pair transactions 
#(TransactionID1, TransacationID2)
pd.merge(transactions,transactions,how='outer',on='UserID')

#20. Join each user to his/her first occuring transaction in the transactions table
users
transactions
user_trans_all = pd.merge(users, transactions, how='left', on='UserID')
user_trans_all.drop_duplicates(subset='UserID',keep='first').reset_index(drop=True)

#21. Test to see if we can drop columns
#Retieve the column list for the dataframe df_ created in problem statement 20
my_columns = list(user_trans_all.columns)
my_columns
#set threshold to drop NAs
list(user_trans_all.dropna(thresh=int(user_trans_all.shape[0] * .9), axis=1).columns)
#missing_info
missing_info = list(user_trans_all.columns[user_trans_all.isnull().any()])
missing_info
for col in missing_info:
#count number missing for column
    num_missing = user_trans_all[user_trans_all[col].isnull() == True].shape[0]
    print('number missing for column {}: {}'.format(col, num_missing))
#count of missing user_trans_all for col in missing_info: 
    percent_missing = user_trans_all[user_trans_all[col].isnull() == True].shape[0] / user_trans_all.shape[0]
    print('percent missing for column {}: {}'.format(col, percent_missing))
