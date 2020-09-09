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

# Count Each Canidates Total Votes
    
    vt_khan=0
    vt_otooley=0
    vt_correy=0
    vt_li=0

    for i in range(1,len(canidates)): 
        if canidates[i]=='Khan':
            vt_khan=vt_khan+1   
        
    for j in range(1,len(canidates)):
        if canidates[j]=='Correy':
            vt_correy=vt_correy+1
        
    for k in range(1,len(canidates)):    
        if canidates[k]=='Li':
            vt_li=vt_li+1   

    for l in range(1,len(canidates)):    
        if canidates[l]=="O'Tooley":
            vt_otooley=vt_otooley+1

t_votes=len(canidates)

a=vt_khan
b=vt_otooley   
c=vt_correy
d=vt_li

#final_count=max("Khan":a, "O'Tooley":b, "Correy":c, "Li":d, keys())

print("Election Results")
print("-------------------------")
print(f"Total Votes: {t_votes}")
print("-------------------------")
print(f"Khan: {round((vt_khan/t_votes)*100)}% {vt_khan}")
print(f"Correy:{round((vt_correy/t_votes)*100)}% {vt_correy}")
print(f"Li: {round((vt_li/t_votes)*100)}% {vt_li}")
print(f"O'Tooley: {round((vt_otooley/t_votes)*100)}% {vt_otooley}")
print("-------------------------")
#print(f"Winner: {final_count}")
print("-------------------------")


output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as writer:

    writer.write("Election Results\n")
    writer.write("-------------------------\n")
    writer.write(f"Total Votes: {t_votes}\n")
    writer.write("-------------------------\n")
    writer.write(f"Khan: {round((vt_khan/t_votes)*100)}% {vt_khan}\n")
    writer.write(f"Correy:{round((vt_correy/t_votes)*100)}% {vt_correy}\n")
    writer.write(f"Li: {round((vt_li/t_votes)*100)}% {vt_li}\n")
    writer.write(f"O'Tooley: {round((vt_otooley/t_votes)*100)}% {vt_otooley}\n")
    writer.write("-------------------------\n")
    #writer.write(f"Winner: {max( final_count.keys() )}\n")
    writer.write("-------------------------\n")