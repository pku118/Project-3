import pandas as pd
from sqlalchemy import create_engine

# Load data
companies = pd.read_csv('data/sp500_companies.csv')
stocks = pd.read_csv('data/sp500_stocks.csv')
index = pd.read_csv('data/sp500_index.csv')

# Convert 'Date' columns to datetime
stocks['Date'] = pd.to_datetime(stocks['Date'])
index['Date'] = pd.to_datetime(index['Date'])

# Combine data
data = stocks.merge(companies[['Symbol', 'Shortname']], on='Symbol')


# Save to SQLite database
db_path = "sqlite:///sp500_data.db"
engine = create_engine(db_path)
data.to_sql('stocks', engine, index=False, if_exists='replace')
index.to_sql('sp500', engine, index=False, if_exists='replace')
print("Data processing and database creation completed successfully.")