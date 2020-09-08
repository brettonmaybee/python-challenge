import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
    

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)

    #total_months =sum(1 for row in csvfile)
    total_months=len(csvreader)
    
 
with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)   
    
    profits_losses=[]

    for row in csvreader: 
        profits_losses.append(row[1])

p_l_int=[int(i) for i in profits_losses]

def sum(data):
    total=0
    for x in data:
        total += x
    return total

total=sum(p_l_int)


def mean(data):
    total=0
    for x in data:
        total +=x
        average=total/len(data)
    return average

average=mean(p_l_int)


def change(data):
    total=0
    for x in data:
        total +=x
        mean=total/len(data)
        data[:] = [i - mean for i in data]
    return data


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")"
print(f"Total: ${total}")
print(f"Average  Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_row[0]} ${max_row[1]}")
print(f"Greatest Decrease in Profits: {min_row[0]} ${min_row[1]}")