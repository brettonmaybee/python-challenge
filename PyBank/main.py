import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


   
with open(csvpath, 'r') as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    date =[]
    profit_loses=[]
    change=[]

    for row in csvreader:

        profit_loses.append(float(row[1]))
        date.append(row[0])

    for i in range(1,len(profit_loses)): 
        
        change.append(profit_loses[i] - profit_loses[i-1])   
        
        avg_change = sum(change)/len(change)

        max_change = max(change)

        min_change = min(change)

        max_change_date = str(date[change.index(max(change))])
        min_change_date = str(date[change.index(min(change))])
   
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${sum(profit_loses)}")
print(f"Average Change: ${round(avg_change)}")
print(f"Greatest Increase in Profits: {max_change_date} ${max_change}")
print(f"Greatest Decrease in Profits: {min_change_date} ${min_change}")

output_path = os.path.join("analysis", "analysis.txt")



with open(output_path, 'w') as writer:
 
    writer.write("Financial Analysis\n")
    writer.write("----------------------------\n")
    writer.write(f"Total Months: {len(date)}\n")
    writer.write(f"Total: ${sum(profit_loses)}\n")
    writer.write(f"Average Change: ${round(avg_change)}\n")
    writer.write(f"Greatest Increase in Profits: {max_change_date} ${max_change}\n")
    writer.write(f"Greatest Decrease in Profits: {min_change_date} ${min_change}\n")
