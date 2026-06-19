#import pandas library as pd
import pandas as pd

# Load time series data
df = pd.read_csv('time_series_data.csv')

# Print the shape (Rows, Columns)
print("--- Table Shape ---")
print(df.shape) 

# See the first 5 rows of the data
print("\n--- First 5 Rows ---")
print(df.head())
