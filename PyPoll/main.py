import os
import csv

# Log file address in py_poll_csv
py_poll_csv = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Add variables
total_ballots = 0
#Create dictionary to hold candidates' names as keys and results as values
candidate_ballots={}

# Scan CSV file
with open(py_poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Start after the row containing headers
    next(csvreader)

    #Read every row in the file
    for row in csvreader:
               
        #Add all ballots
        total_ballots += 1
        #Capture unique candidates names - replace candidates with candidate_names
        candidate_name=row[2]
        if candidate_name not in candidate_ballots:
            candidate_ballots[candidate_name]=0

        #Count the ballots for each candidate
        candidate_ballots[candidate_name]+=1

    #Print results
    print('Election Results')
    print('-------------------------------------------')
    print(total_ballots)
    print('-------------------------------------------')
    #Print dictionary keys and values in separate rows:
    for key, value in candidate_ballots.items():
        rate=round(value/total_ballots*100,3)
        print(key,": ",value, "(",rate,"%)")
    print('-------------------------------------------')
    winner_name=max(candidate_ballots,key=candidate_ballots.get)  
    print('Winner:', winner_name)

    #Create file
    with open('Analysis.txt','w') as f:
        f.write('Election Results')
        f.write('\n')
        f.write('-------------------------------------------')
        f.write('\n')
        f.write('Total ballots: ')
        f.write(str(total_ballots))
        f.write('\n')
        f.write('-------------------------------------------')
        f.write('\n')
        for key, value in candidate_ballots.items():
            rate=round(value/total_ballots*100,3)
            #Define tuple
            summary=str(key),": ",str(value), "(",str(rate),"%)"
            #Create empty string
            st=''
            #Using loops to convert tuple into string
            for item in summary:
                st= st + item
            f.write(st)
            f.write('\n')
        f.write('-------------------------------------------')
        f.write('\n')
        f.write('Winner: ')
        f.write(winner_name)



