# Add dependencies

import csv

import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable for the file to save and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Declare dictionary
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with  open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

# Read the header row
    headers = next(file_reader)

# Print each row in the CSV file
    for row in file_reader:
    
        # Add to the total vote count
            total_votes +=1 #ask tutor what this is

    # Print the candidate name from each row
            candidate_name = row[2]

    # Add candidate name to the candidate list
            if candidate_name not in candidate_options:

            # Add to list of candidates
                candidate_options.append(candidate_name)

        # Begin tracking candidates' votes
                candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n")

    print(election_results,end="")

    # Save the final vote count to the text file

    txt_file.write(election_results)

    for candidate_name in candidate_votes:
            # Calculate vote pct

        votes = candidate_votes[candidate_name]

        vote_percentage = (float(votes) / float(total_votes)) * 100
        
    # Print candidate vote dictionary
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)

# Determine winning vote count and candidate 

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true then set winning_count = votes and winning_percent = vote_percentage

            winning_count = votes
            winning_percentage = vote_percentage

            # Set the winning_candidate = candidate's name

            winning_candidate = candidate_name

        # Print out winning candidate, vote count and pct to terminal

    winning_candidate_summary = (f"--------------------------_\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n") 

    print(winning_candidate_summary)

    # Save winning candidate results to text file
    txt_file.write(winning_candidate_summary)