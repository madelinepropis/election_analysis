# Election Analysis

## Overview of Project

The purpose of this analysis was to audit a congressional election for a precinct in Colorado. The data given included a CSV file containing ballot ID, county and Candidate choice. Python is used to breakdown the data to determine the number and percentage of votes, winning candidate, number and percentage of counties in the precinct, and largest county.

## Election-Audit Results

### Analysis of Vote Count

There are 369,711 votes being analyzed in this challenge. This number was found with the code "total_votes = total_votes + 1" within a for loop. This loop ran through all votes and adds a new vote to the total count each time the loop is passed.

### Vote Breakdown

Like the vote count, the number of votes and percentage of votes for each county was determined using for loops. The number of votes was found with the code "county_votes[county] += 1". Using the code "vote_percentage = (float(votes) / float(total_votes)) * 100", the vote percentage for each county was determined.

The votes by county breakdown follows:

Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

As displayed, Denver had the largest number of votes.

### Candidate Breakdown

Another use for for loops in this analysis was for the candidate breakdown. The code provides the breakdown of the number of votes and percentage of total votes that each candidate received. The number of votes was found with the code "votes = candidate_votes.get(candidate_name)". Using the code "vote_percentage = float(votes) / float(total_votes) * 100", the vote percentage for each candidate was determined.

The votes for each candidate is below:

Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

As displayed, Diana DeGette won the election. She won with 272,892 votes, which was 73.8% of the total votes. 

## Election-Audit Summary

This Python script can be used for any election only with some modifications. This can be done for presidential election with only changing the names of "counties" to "states". Additionally, more candidates and counties could be added. By changing names and numbers of specific variables such as candidate count, this script can be modified for any election. 
