#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:12:59 2019

@author: admin
"""

# Import Modules/Dependencies
import os
import csv

# Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Set Path For File
csvpath = os.path.join('election_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:

    # read csv separating by commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header
    csv_header = next(csvfile)

    # read csv per row
    for row in csvreader:
        
        # add up total votes
        total_votes += 1
        
        # add up individual votes
        if (row[2] == "Khan"):
            khan_votes = khan_votes 1
        if (row[2] == "Correy"):
            correy_votes += 1
        if (row[2] == "Li"):
            li_votes += 1
        if (row[2] == "Otooley"):
            otooley_votes += 1
            
    # Calculate Percentage Of Votes Each Candidate Won
    kahn_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    # Calculate Winner Of The Election Based On Popular Vote
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")