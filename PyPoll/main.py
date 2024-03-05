import os #imports library to specify the csv file's path in the OS
import csv #imports library to read and process the csv file

electiondata_csv = os.path.join("Resources", "election_data.csv") #specifices the file's path for the .py file to locate and open it

#initialize the variables
total_votes = 0
vote_count = {} #this variable will store vote counts for each candidate, as well as the candidate names.

with open(electiondata_csv,'r') as csvfile: #open the file in read mode
     csvreader = csv.reader(csvfile)
     next (csvreader) #Skip the header

     for row in csvreader: #iterate through all rows
         candidate_name = row[2] #specify candidate's name is in column #2
         vote_count[candidate_name] = vote_count.get(candidate_name, 0) + 1 #checks if a candidate's name exists in the vote_count dictionary, and if so, increments the existing vote count by 1. If not, it returns the defauls value of 0.
         total_votes += 1 #increment the total vote count

print('''Election Results
---------------------''')
print (f"Total Votes: {total_votes}")
print ('''--------------------- ''')


# Calculate and print the percentage of votes for each candidate
for candidate, votes in vote_count.items():
     percentage = (votes / total_votes) * 100
     print(f"{candidate}: {percentage:.3f}% ({votes})")

print ('''---------------------''')

winner = max(vote_count, key=vote_count.get)

print("Winner:", winner)

print ('''---------------------''')

# Export analysys to a text file

output_file = "election_results.txt"
with open(output_file,"w") as text_file:
    text_file.write("Election Results\n") # the \n is used to input a new line (space)
    text_file.write("--------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("--------------------------\n")
    for candidate, votes in vote_count.items():
         percentage = (votes / total_votes) * 100 
         text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n") #instead of print, we use text_file.write but it is still an iteration 
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")

    # Prints a message indicating that the file has been written
print(f"Results have been written to {output_file}")