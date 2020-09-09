import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

def ballet_data()
    id=[0]
    county=[1]
    name=[2]

    
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
    #   print(row)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {}% {vt_Khan}")
print(f"Correy:{}% {vt_Corry}")
print(f"Li: {}% {(vt_Li}")
print(f"O'Tooley: {}% {vt_Otooley}")
print("-------------------------")
print(f"Winner: {most_vost}")
print("-------------------------")
