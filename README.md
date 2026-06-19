# Exploring_Pandas
This project entails data cleaning guide using Pandas. The script loads a time-series dataset, standardizes headers to lowercase, converts text dates into actual timestamp objects, fixes missing data (NaNs), filters out impossible sensor temperatures, removes duplicates, and exports a cleaned CSV file.
# Data Processing Steps Explained

1. **Advanced File Reading:** Loads the CSV dataset, explicitly sets commas as delimiters, and converts the raw row counter into a clean index column.
2. **Header Standardization:** Strips whitespace and forces column names to lowercase, transforming `Temperature` into a clean, unit-aware heading (`temp_celsius`).
3. **Datetime Conversion:** Parses string text dates into native datetime objects, unlocking time-series features.
4. **Missing Value Management:** Fills empty cells with fallback numbers and removes critical gaps using a combination of `fillna()` and `dropna()`.
5. **Data Outlier Filtering:** Caps extreme sensor error spikes at a baseline and slices out values outside realistic operational limits (-50°C to 60°C).
6. **Deduplication:** Purges identical rows recorded due to transmission overlaps using `drop_duplicates()`.

## Pipeline Execution Results

When the script executes on the raw `time_series_data.csv`, it processes the table records and produces the following terminal output:

```text
--- Final Cleaned Table Shape ---
(366, 3)

--- First 5 Rows of Cleaned Data ---
            date  temp_celsius    month
0     2020-01-01     27.483571  January
1     2020-01-02     24.308678  January
2     2020-01-03     28.238443  January
3     2020-01-04     32.615149  January
4     2020-01-05     23.829233  January

Success! 'cleaned_time_series_data.csv' has been created.

Output File

The script automatically exports the final, structured dataset into a clean, deployment-ready file named cleaned_time_series_data.csv.
