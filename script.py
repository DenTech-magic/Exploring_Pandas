
import pandas as pd

# Load the file and use the very first column as the row index labels
df = pd.read_csv('time_series_data.csv', index_col=0, sep=',')

# Convert all column text headers to lowercase and strip out any accidental spaces
df.columns = df.columns.str.lower().str.strip()

# Change the specific column header name from 'temperature' to 'temp_celsius'
df = df.rename(columns={'temperature': 'temp_celsius'})

# Transform the date column from plain text strings into actual date-time objects
df['date'] = pd.to_datetime(df['date'])

# Look for any blank entries in the temperature column and fill them with 0
df['temp_celsius'] = df['temp_celsius'].fillna(0)

# Drop any rows from the table where the date or temperature is completely missing
df = df.dropna(subset=['date', 'temp_celsius'])

# Find any unrealistic sensor error temperatures above 100 and reset them to 25.0
df.loc[df['temp_celsius'] > 100, 'temp_celsius'] = 25.0

# Filter the table to only keep rows where temperatures are between -50 and 60 degrees
df = df[(df['temp_celsius'] >= -50) & (df['temp_celsius'] <= 60)]

# Scan the entire table and delete any rows that are exact duplicates of previous rows
df = df.drop_duplicates()

# Read the fixed dates and pull out the text name of the month into a new column
df['month'] = df['date'].dt.month_name()

# Display the final rows and columns count of the cleaned table on the screen
print("Cleaned Time-Series Dataset")
print(df.shape)

# Display a quick preview of the top 5 rows of the processed data
print("\n--- Cleaned Time-Series Dataset ---")
print(df.head())

# Export the entire cleaned table into a brand new CSV file inside the project folder
df.to_csv('cleaned_time_series_data.csv', index=True)

