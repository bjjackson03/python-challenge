#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:12:33 2019

@author: admin
"""

import os
import csv

#setpath for retrieval
csvpath = os.path.join("election_data.csv")

#variables
#captures candidates, percentage of votes, how many votes per candidate, total number of votes
runners = []
percent_of_votes = []
votes_per_runner = []
vote_total = 0

#open csv and skips header row
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        #run thru each row
        vote_total = vote_total + 1 
        
        #locate names and store them in an index: runners
        if row[2] not in runners:
            runners.append(row[2])
            index = runners.index(row[2])
            votes_per_runner.append(1)
        #tally of votes per runner and stores them in an index: votes per runner
        else:
            index = runners.index(row[2])
            votes_per_runner[index] += 1
    
    #converts to percent and stores value 
    for votes in votes_per_runner:
        percent = (votes/vote_total) * 100
        percent = round(percent)
        percent = "%.2f%%" % percent
        percent_of_votes.append(percent)
    
    #winning runner
    first_place = max(votes_per_runner)
    index = votes_per_runner.index(first_place)
    winner = runners[index]

#output to a new csv
with open('election_results.csv', 'w+') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Election Results"])
    writer.writerow(["---------------------"])
    writer.writerow(["Total Votes: " + str(vote_total)])
    writer.writerow(["---------------------"])
    writer.writerow([str(runners[0]) + ": " + str(percent_of_votes[0]) + " " + "(" + str(votes_per_runner[0]) + ")."])
    writer.writerow([str(runners[1]) + ": " + str(percent_of_votes[1]) + " " + "(" + str(votes_per_runner[1]) + ")."])
    writer.writerow([str(runners[2]) + ": " + str(percent_of_votes[2]) + " " + "(" + str(votes_per_runner[2]) + ")."])
    writer.writerow([str(runners[3]) + ": " + str(percent_of_votes[3]) + " " + "(" + str(votes_per_runner[3]) + ")."])
    writer.writerow(["---------------------"])
    writer.writerow(["Winner: " + str(winner) ])
    writer.writerow(["---------------------"])
    
#prints out in console back from new csv created
with open('election_results.csv', 'r') as readfile:
    print(readfile.read())