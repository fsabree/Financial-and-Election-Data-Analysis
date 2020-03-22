# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

import os
import csv

election_data_csv_path = os.path.join(".", "Resources", "election_data.csv")

total_votes = []
candidate_correy = []
candidate_khan = []
candidate_li = []
candidate_otooley = []

with open(election_data_csv_path) as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")

     # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)       
    # Read through each row of data after the header

    # The total number of votes cast
    for row in csv_reader:
        total_votes.append(row[0])

    # A complete list of candidates who received votes plus getting the count of votes for each candidate
        if row[2] == "Correy":
            candidate_correy.append(row[2])  
            
        elif row[2] == "Khan":
            candidate_khan.append(row[2])

        elif row[2] == "Li":
            candidate_li.append(row[2])

        elif row[2] == "O'Tooley":
            candidate_otooley.append(row[2])

# The percentage of votes each candidate won

correy_vote_percentage = (len(candidate_correy)/len(total_votes))*100
khan_vote_percentage = (len(candidate_khan)/len(total_votes))*100
li_vote_percentage = (len(candidate_li)/len(total_votes))*100
otooley_vote_percentage = (len(candidate_otooley)/len(total_votes))*100

# The winner of the election based on popular vote.

# Create a dictionary with the candidates and vote percentage wins.
candidates = {"names":["Correy","Khan","Li","O'Tooley"],
             "vote_percentage":[correy_vote_percentage,
                                khan_vote_percentage,
                                li_vote_percentage,
                                otooley_vote_percentage]
             }

# Find the index for the max vote percentage from dictionary and then found the corresponding winner name.
winner_index_key = candidates["vote_percentage"].index(max(candidates["vote_percentage"]))
winner = candidates["names"][winner_index_key]


print("Election Results")
print("-"*25)
print(f"Total Votes: {len(total_votes)}")
print("-"*25)
print(f"Correy: {round(correy_vote_percentage,2)}% Total Votes: ({len(candidate_correy)})")
print(f"Khan: {round(khan_vote_percentage,2)}% Total Votes: ({len(candidate_khan)})")
print(f"Li: {round(li_vote_percentage,2)}% Total Votes: ({len(candidate_li)})")
print(f"O'Tooley: {round(otooley_vote_percentage,2)}% Total Votes: ({len(candidate_otooley)})")
print("-"*25)
print(f"Winner: {winner}")

text_file = open("election_summary_output.txt", "w")
text_file.write("Election Results\n")
text_file.write("-"*25)
text_file.write(f"\nTotal Votes: {len(total_votes)}\n")
text_file.write("-"*25)
text_file.write(f"\nCorrey: {round(correy_vote_percentage,2)}% Total Votes: ({len(candidate_correy)})\n")
text_file.write(f"Khan: {round(khan_vote_percentage,2)}% Total Votes: ({len(candidate_khan)})\n")
text_file.write(f"Li: {round(li_vote_percentage,2)}% Total Votes: ({len(candidate_li)})\n")
text_file.write(f"O'Tooley: {round(otooley_vote_percentage,2)}% Total Votes: ({len(candidate_otooley)})\n")
text_file.write("-"*25)
text_file.write(f"\nWinner: {winner}\n")
text_file.close()