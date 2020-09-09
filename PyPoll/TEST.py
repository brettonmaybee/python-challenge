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
    votes_per_can = [None] * len(canidates);    
    counted = -1;

    for i in range(0, len(canidates)):    
        count = 1;    
    for j in range(i+1, len(canidates)):    
        if(canidates[i] == canidates[j]):    
            count = count + 1;    
            #To avoid counting same element again    
            votes_per_can[j] = counted;    
                
    if(votes_per_can[i] != visited):    
        votes_per_can[i] = count;    
    
    #Displays the frequency of each element present in array    
        print("---------------------");    
        print(" Canidate | Votes");    
        print("---------------------");    
    for i in range(0, len(votes_per_can)):    
        if(votes_per_can[i] != visited):    
            print("    " + str(canidates[i]) + "    |    " + str(votes_per_can[i]));    
            print("---------------------");    
    #for i in range(1,len(csvreader)):


