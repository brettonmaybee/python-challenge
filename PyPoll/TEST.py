import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Create sperate lists from the election data
    reg_num=[]
    county=[]
    canidates=[]

    for row in csvreader:

        reg_num.append(int(row[0]))
        county.append(row[1])
        canidates.append(row[2])

# Check for duplicate voter id numbers
    def dupcheck(list):
    
        if len(list) == len(set(list)):
            return "No duplicate id numbers"
        else:
            return True
       
    print(dupcheck(reg_num))
    
# Identify the canidates
    
    canidates_set=set(canidates)

    print(canidates_set)



    #for c in canidates:
    
    #for i in range(1,len(csvreader)):


