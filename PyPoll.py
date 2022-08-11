# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote

# Add dependencies

import csv

import os
from re import I 

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable for the file to save and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with  open(file_to_load) as election_data:

# Using the open statement to open the file as a text file
#ith open(file_to_save, "w") as txt_file:

# Write three counties to the file
    #txt_file.write("Counties in the Election\n_________________________\nArapahoe\nDenver\nJefferson")

# Read the file object with the reader function
    file_reader = csv.reader(election_data)

# Print the header row
    headers = next(file_reader)

    print(headers)

# Print each row in the CSV file
    #for row in file_reader:
        #print(row[0])