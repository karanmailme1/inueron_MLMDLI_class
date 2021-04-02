# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 01:41:58 2021
@author: 17jan

python program practice 4
"""

import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)


# Q1.1.
# create a sample JSON object from titanic train dataset
# https://raw.githubusercontent.com/pcsanwald/kaggle-titanic/master/train.csv
df = pd.read_csv('https://raw.githubusercontent.com/pcsanwald/kaggle-titanic/master/train.csv')
df.shape
df.head()
df.to_json('test_json1.json')


# Q1.2.
# Read the JSON object and convert it to pandas data frame
df1 = pd.read_json('test_json1.json').fillna(np.nan)
df1.shape
df1.head()


# Q1.3.
# match the top 5 records from JSON read and actual titanic dataset
df.head() == df1.head()
df.head()
df1.head()


# Q2.1.
# read the HTML file as given below
# http://vincentarelbundock.github.io/Rdatasets/datasets.html
html_obj = pd.read_html('http://vincentarelbundock.github.io/Rdatasets/datasets.html')
html_obj[1].shape
html_obj[1].head()


# Q2.2.
# create a data frame from the above object
df2 = html_obj[1]
type(df2)

# Q2.3.
# Create URL to JSON file (alternatively this can be a filepath)
#url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json'
df3 = pd.read_json('https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json')
df3.head()
df3.info()


