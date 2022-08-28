# The data we need to retrieve:
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# import dependancies (csv and os modules)
import csv
import os

# Set total_votes to 0
total_votes = 0

# Create new list to hold candidate names:
candidate_options = []

# Create dictionary to hold votes per candidate:
candidate_votes = {}

# Create winning candidate tracker variables:
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Assign a variable to load the file from a path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: perform analysis
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read the header row
    headers = next(file_reader)
    
    # Iterate through the file
    for row in file_reader:

        # Tabulate the votes
        total_votes += 1

        # Read the candidate name
        candidate_name = row[2]

        # Check if the candidate is already in the candidate list:
        if candidate_name not in candidate_options:
            
            # If not, add candidate to the candidate list:
            candidate_options.append(candidate_name)

            # Start tracking votes for the candidate:
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's counts:
        candidate_votes[candidate_name] += 1

# Save the results to a file:
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final result to the file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the candidate votes dictionary
    # 1. Iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count:
        votes = candidate_votes[candidate_name]

        # Calculate % of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print results per candidate:
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        
        # Save candidate results to the text file:
        txt_file.write(candidate_results)

        
        # Determine winning vote count, percentage and candidate:
        if votes > winning_count and vote_percentage > winning_percentage:

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name
        
    # Print winning candidate results
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning vote count: {winning_count:,}\n"
    f"Winning percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    print(winning_candidate_summary)
    
    # Save results to the text file:
    txt_file.write(winning_candidate_summary)


