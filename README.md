# Welcome to the Pandas Time-Series Data Cleaning Project! 👋

This repository demonstrates how to load, clean, and structure raw environmental logs using Python and pure **Pandas**. 

Instead of relying on heavy external software, this script sets up an automated cleaning pipeline to transform a messy, raw sensor file into a structured dataset.

---

## 🛠️ The Data Powerhouse: What the Code Does

This pipeline automatically cleans and fixes the data using three main steps:

* **Text and Header Fixing:** It strips out accidental empty spaces, forces all column names to lowercase, and renames the temperature column to `temp_celsius` so the units are crystal clear.
* **Smart Data Filtering:** It changes text dates into real date objects, fills missing blank cells with safe baseline values, and deletes exact clone rows caused by transmission errors.
* **Error and Gap Cleaning:** It flags impossible hardware temperature spikes, resets them to a realistic baseline, crops values to safe limits (-50°C to 60°C), and pulls out the text name of the month into a new column.

---

## Pipeline Execution Results

When the script executes on the raw `time_series_data.csv`, it processes the table records and produces the following terminal output:

```text
--- Final Cleaned Table Shape ---
(366, 3)

--- First 5 Rows of Cleaned Data ---
        date  temp_celsius    month
0 2020-01-01     27.483571  January
1 2020-01-02     24.308678  January
2 2020-01-03     28.238443  January
3 2020-01-04     32.615149  January
4 2020-01-05     23.829233  January
