# Original .csv had data from 2010, due to the limitation of github file upload(100mb) we needed to eliminate some data.

import pandas as pd

# Read the original CSV file
original_csv_file = "data/sp500_stocks.csv"
df = pd.read_csv(original_csv_file)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Define the date range
start_date = '2018-01-01'
end_date = '2024-02-16'

# Filter the dataframe based on the date range
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Save the filtered data to a new CSV file
filtered_csv_file = "data/sp500_stocks.csv"  
filtered_df.to_csv(filtered_csv_file, index=False)

# Display the first few rows of the filtered dataframe
print("Filtered Data:")
print(filtered_df.head())
