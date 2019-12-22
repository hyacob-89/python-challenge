import os
import csv

# path to collect data from PyBank folder
csvpath=os.path.join('..','PyPoll','election_data.csv')

# read in CSV file as dictionary
PollDict = {}
with open(csvpath, newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile,delimiter=',')
    #csv_header = next(csv_reader)


    print('\nElection Results')
    print('-------------------------')
    
    
    for row in csv_reader:

        if row['Candidate'] in PollDict.keys():
            PollDict[row['Candidate']]+=1
        else:
            PollDict[row['Candidate']]=1
    


    for j in PollDict.values():

        total_votes = sum(PollDict.values())
        

    print(f'Total Votes: {total_votes}')
    print('-------------------------')        
      
    
    for i, j in PollDict.items():

        total_votes = sum(PollDict.values())
        percentage = (j/total_votes)*100
        winner_name = max(PollDict, key = PollDict.get)

        print(f"{i}: {percentage:.3f}% ({j})")   

    print('-------------------------')    
    print(f'Winner: {winner_name}')
    print('-------------------------')



