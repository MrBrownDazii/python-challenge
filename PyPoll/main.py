# Modernzing a voting-counting process 
import os
import csv

#Set path of file
csvpath = os.path.join("..","PyPoll","resources","election_data.csv")
file_to_output = "analysis/election_analysis_2.txt"

# Set variables
total_votes = 0
candidate = ""
candidates_list = []
vote_list = []
percent_list = []
winner = ""

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # count the total number of months
        total_votes += 1
        
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidates_list.index(row[2])] += 1

# Percent of vote won per each candiate           
percent_list = [(100/total_votes) * x for x in vote_list]

# Finding winner for the election
winner = candidates_list[vote_list.index(max(vote_list))]

# Print the analysis to terminal       
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for x in candidates_list:
    print(x + ": " + str(format(percent_list[candidates_list.index(x)], '.3f')) 
        + "% (" + str(vote_list[candidates_list.index(x)]) + ")")
    
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Write to text file
f = open("analysis.txt", "w")

f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("-------------------------\n")

for x in candidates_list:
    f.write(x + ": " + str(format(percent_list[candidates_list.index(x)], '.3f')) 
        + "% (" + str(vote_list[candidates_list.index(x)]) + ")\n")
    
f.write("-------------------------\n")
f.write("Winner: " + winner + "\n")
f.write("-------------------------\n")

f.close()