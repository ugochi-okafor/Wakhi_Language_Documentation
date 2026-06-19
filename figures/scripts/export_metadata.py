# Exports simple summary of dataset

import csv

input_file = "../metadata/file_index.csv"

with open(input_file, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
