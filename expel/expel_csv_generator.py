import csv
import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)
from query_generator import QueryGenerator

# Set the name of the CSV file
CSV_FILE = 'expel/coa-query-sample.csv'
NUM_ROWS = 100

# Initialize a QueryGenerator object
qg = QueryGenerator()

# Generate the supporting information and store it in a list
supporting_info_list = []
for _ in range(NUM_ROWS):
    supporting_info = qg.generate_troops()
    supporting_info_list.append([supporting_info])

# Write the data to a CSV file
with open(CSV_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["supporting_information"])  # Write the header
    writer.writerows(supporting_info_list)

# Confirm that the CSV has been generated
print(f"CSV file '{CSV_FILE}' has been created with {NUM_ROWS} rows.")