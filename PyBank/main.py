import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
    
with open(csvpath) as csvfile:
    
    row_count =sum(1 for row in csvfile)

print (f"Total Months: {row_count-1}")

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header=next(csvreader)

    profits_losses=[int()]

    for row in csvreader: 
        profits_losses.append(row[1])

profits_losses=[int(i) for i in profits_losses]

def sum(data):
    total=0
    for row in data:
        total += row
    return total

total=sum(profits_losses)

print(total)



