#The overall purpose of this script is to clean the raw data from sales_data_raw.csv with the assistance 

import pandas as pd
import numpy as np

sales_df = pd.read_csv('ism2411-data-cleaning-copilot/data/raw/sales_data_raw.csv')

print(sales_df)
#Standardize column names to uppercase
#Ensure all column names are in uppercase for consistency and ease of reading
#Ensure there are no leading or trailing spaces in column names
#Apply the new standardized column names to the DataFrame
sales_df.columns = sales_df.columns.str.upper().str.strip()


#Remove leading and trailing spaces from string entries in the 'PRODNAME' and 'CATEGORY' column
#This step ensures that product names and categories are clean and free from unwanted spaces that could affect data analysis
#apply the new cleaned string entries back to the DataFrame

sales_df['PRODNAME'] = sales_df['PRODNAME'].str.strip()
sales_df['CATEGORY'] = sales_df['CATEGORY'].str.strip()

print(sales_df)









