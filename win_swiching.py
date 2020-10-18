import csv
import pprint

with open('win_pingresult.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)