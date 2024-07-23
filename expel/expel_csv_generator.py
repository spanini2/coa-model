import csv
import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)
from query_generator import QueryGenerator

# Set the name of the CSV file
# CSV_FILE = 'expel/coa-query-sample.csv'
# NUM_ROWS = 100

# Use these constants for the small sample
CSV_FILE = 'expel/coa-query-small-sample.csv'
NUM_ROWS = 10

# Initialize a QueryGenerator object
qg = QueryGenerator()

# Generate the queries and store it in a list
queries = []
for _ in range(NUM_ROWS):
    question = "Can you help me generate a military course of action given the support information?"
    supporting_info = qg.generate_troops()

    # Use this line for the big sample
    # queries.append([question, supporting_info])

    # Use this line for the small sample
    queries.append([f"{question}\nSupporting Information:\n{supporting_info}", supporting_info])
    

# Write the data to a CSV file
with open(CSV_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["question", "supporting_information"])  # Write the header
    writer.writerows(queries)

# Confirm that the CSV has been generated
print(f"CSV file '{CSV_FILE}' has been created with {NUM_ROWS} rows.")