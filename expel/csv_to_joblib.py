import pandas as pd
import joblib

# Step 1: Read the CSV file into a DataFrame
csv_file_path = '/home/luke-skywalker/github/coa-model/expel/coa-query-1friendly-1enemy.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Save the DataFrame as a joblib object
joblib_file_path = '/home/luke-skywalker/github/coa-model/expel/coa-query-1friendly-1enemy.joblib'
joblib.dump(df, joblib_file_path)

print(f"CSV file has been successfully converted to a joblib object and saved as {joblib_file_path}")
