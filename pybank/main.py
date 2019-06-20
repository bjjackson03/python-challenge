#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:46:43 2019

@author: admin
"""

import os
import csv

#create path to csv and assign it
csvpath = os.path.join("budget_data.csv")

#open data as csv
with open(csvpath, 'r', newline='') as csvfile:    
    #use reader to open and separate based off of commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #variables to hold data
    months = []
    Revenue = 0
    Inc_Max = 0
    Dec_Min = 0
    
    #Loop through csv w variables being assigned
    for row in csvreader:
        #determines which month we made the most money
        if(Inc_Max<int(row[1])):
            Inc_Max = int(row[1])
            Inc_Max_Month = row[0]
        
        #determines which month we lost the most money
        if(Dec_Min>int(row[1])):
            Dec_Min = int(row[1])
            Dec_Min_Month = row[0]
      
        #total number of months in file
        months.append(row[0])
        #assign variable to total month count
        all_months = len(months)
        #will add up all values in row 2 for rev
        Revenue = Revenue + int(row[1])
    
#output to a new csv
with open('summary.csv', 'w+') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------------"])
    writer.writerow(["Total Months: " + str(all_months)])
    writer.writerow(["Total:" + str(Revenue)])
    writer.writerow(["Average Change:" + str(round(Revenue/all_months, 2))])
    writer.writerow(["Greatest Increase In Profits:" + str(Inc_Max_Month) + " " + str(Inc_Max) ])
    writer.writerow(["Greatest Decrease In Profits:" + str(Dec_Min_Month) + " " + str(Dec_Min) ])
    
#prints out in console back from new csv created
with open('summary.csv', 'r') as readfile:
    print(readfile.read())
    