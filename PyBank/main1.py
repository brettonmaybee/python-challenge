import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
    

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)

    total_months =sum(1 for row in csvfile)
     
with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)   
    
    profits_losses=[]

    for row in csvreader: 
        profits_losses.append(row[1])

p_l=[int(i) for i in profits_losses]

def monthly_budget(budget_data) 
    month=str(budget_data[0])
with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')

    csv_header=next(csvreader)        

    monthly_change=[]

    change=0.0
    total_change=0
    average_change=0
    greatest_increase=0
    smallest_increase=0        

#calculate the change in profit/loss
    
    for row in range(1,len(p_l)):
        change = p_l[row] - p_l[row-1]
        monthly_change.append(change)

#if this is the first year, set trackers to its value
    if row==1:
        greatest_increase = change
        smallest_increase = change
        greatest_month =csvreader([1]:[0])
        smallest_month = csvreader([1]:[0])
#this is not the first change in population size
#update the trackers if relevent
    else:
        if change>greatest_increase:
            greatest_increase = change
            greatest_month = csvreader([row]:[0])
        elif change<smallest_increase:
            smallest_increase = change
            smallest_month = csvreader([row]:[0])
            total_change = float(sum(monthly_change))
            average_change = total_change/86

print("Financial Analysis")
print("----------------------------")
#print(f"Total Months: {total_months}")
#print(f"Total: ${total}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {csvfile[2:0]} ${csvfile[5:1]}")
#print(f"Greatest Decrease in Profits: {min_row[0]} ${min_row[1]}")