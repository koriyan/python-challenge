import os
import csv

# Define the variables

total_votes = 0
candidates = []
vote_counts = []
percentages = []

# Read using csv module
fpath = os.path.join('..',"PyPoll",'Resources','election_data.csv')

# Get data from the csv file
with open(fpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header
    next(csvreader)

    # Loop through the csv file
    for row in csvreader:

        total_votes += 1

        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] += 1

        else:
            candidates.append(candidate)
            vote_counts.append(1)

# To find the winner
max_votes = vote_counts[0]
max_index = 0

for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/total_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count

winner = candidates[max_index]

#print results to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]:.3f}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# Export an analysis text file
write_file = f"Analysis.txt"
analysis = open(write_file, mode = 'w')

analysis.write("Election Results\n")
analysis.write("--------------------------\n")
analysis.write(f"Total Votes: {total_votes}\n")
analysis.write("--------------------------\n")
for count in range(len(candidates)):
    analysis.write(f"{candidates[count]}: {percentages[count]:.3f}% ({vote_counts[count]})\n")
analysis.write("---------------------------\n")
analysis.write(f"Winner: {winner}\n")
analysis.write("---------------------------\n")

analysis
