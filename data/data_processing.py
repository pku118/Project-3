import pandas as pd

# Load data from CSV files
companies = pd.read_csv('data/sp500_companies.csv')
stocks = pd.read_csv('data/sp500_stocks.csv')

# Merge data on 'Symbol'
merged_data = pd.merge(stocks, companies[['Symbol', 'Shortname']], on='Symbol', how='left')

# Save merged data to a SQLite database
import sqlite3

conn = sqlite3.connect('stocks.db')
merged_data.to_sql('stocks_data', conn, index=False, if_exists='replace')
conn.close()