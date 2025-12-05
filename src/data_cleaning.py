#The overall purpose of this script is to clean the raw data from sales_data_raw.csv

import pandas as pd
import numpy as np

sales_df = pd.read_csv('ism2411-data-cleaning-copilot/data/raw/sales_data_raw.csv')

print(sales_df)
#Standardize column names to uppercase
#Ensure all column names are in uppercase for consistency and ease of reading
#Ensure there are no leading or trailing spaces in column names
#Apply the new standardized column names to the DataFrame

def clean_column_names(df):
    df.columns = df.columns.str.upper().str.strip()
    return df
sales_df = clean_column_names(sales_df)


#Standardize string entries in 'PRODNAME' and 'CATEGORY' columns to title case
#This will make the values easier to read and more consistent for analysis
sales_df['PRODNAME'] = sales_df['PRODNAME'].str.title()
sales_df['CATEGORY'] = sales_df['CATEGORY'].str.title()



#Remove leading and trailing spaces from string entries in the 'PRODNAME' and 'CATEGORY' column
#This step ensures that product names and categories are clean and free from unwanted spaces that could affect data analysis
#apply the new cleaned string entries back to the DataFrame

sales_df['PRODNAME'] = sales_df['PRODNAME'].str.strip()
sales_df['CATEGORY'] = sales_df['CATEGORY'].str.strip()

#print(sales_df)

#Handle missing values in 'PRICE' column by filling them with the mean price
#Handle missing values in the 'QTY' column by filling them with the median quantity
#Convert 'PRICE' column from string to float, and 'QTY' column from string to integer
#BFill any missing values in 'DATE_SOLD' column with the previous valid entry
#Convert 'DATE_SOLD' column to datetime format
#This step ensures that there are no missing values in these columns, which could affect calculations
sales_df['PRICE'] = pd.to_numeric(sales_df['PRICE'], errors='coerce')
mean_price = sales_df['PRICE'].mean()
sales_df['PRICE'].fillna(mean_price, inplace=True)
sales_df['QTY'] = pd.to_numeric(sales_df['QTY'], errors='coerce')
median_quantity = sales_df['QTY'].median()
sales_df['QTY'].fillna(median_quantity, inplace=True)
sales_df['QTY'] = sales_df['QTY'].astype(int)
sales_df['DATE_SOLD'] = pd.to_datetime(sales_df['DATE_SOLD'], errors='coerce')
sales_df['DATE_SOLD'].fillna(method='bfill', inplace=True)


#Removing rows with negative values
#Negative values are not possible and will cause errors in calculations

def remove_invalid_rows(sales_df):
    sales_df = sales_df[sales_df['PRICE'] > 0]
    sales_df = sales_df[sales_df['QTY'] > 0]
    return sales_df
sales_df = remove_invalid_rows(sales_df)



#Save the cleaned DataFrame to a new CSV file
sales_df.to_csv('ism2411-data-cleaning-copilot/data/processed/sales_data_clean.csv', index=False)
print("Cleaned data saved to sales_data_clean.csv")
print(f"\nFirst few rows of cleaned dataset: \n{sales_df.head()}")







