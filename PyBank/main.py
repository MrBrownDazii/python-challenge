# #Analyzing financial records of your company

import csv
import os

#Setting path for file
csvpath = os.path.join("..","PyBank","resources","budget_data.csv")
file_to_output = "analysis/budget_analysis_1.txt"

# Setting variables
total_months = 0
total_profit_losses = 0
prev_profit_losses = 0
month_change = 0
total_month_change = 0
average_month_change = 0
biggest_increase = 0
biggest_increase_month = ""
biggest_decrease = 0
biggest_increase_month = ""

# Path for opening the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read all the header row in the data first
    csv_header = next(csvreader)
    
    # Read every row data after the header first
    for row in csvreader:
        
        # count the total number of months
        total_months += 1
        
        # add up the total net "profit/losses" over the entire period
        total_profit_losses += int(row[1])
        
        # calculate the change in profit/loss between months
        if total_months > 1:
            month_change = int(row[1]) - prev_profit_losses
            
        # add up the total monthly change, used later to calculate average
        total_month_change += month_change
        
        # set profit/loss value for previous month
        prev_profit_losses = int(row[1])
        
        # calculate biggest increase in profits
        if month_change > biggest_increase:
            biggest_increase = month_change
            greatest_increase_month = row[0]
        
        # calculate biggest decrease in losses
        if month_change < biggest_decrease:
            biggest_decrease = month_change
            biggest_decrease_month = row[0]

# calculate average change between months        
average_month_change = total_month_change / (total_months - 1)

# Print the analysis to terminal
print("Financial Analysis")
print("----------------------------")        
print("Total Months: " + str(total_months))
print("The Total: $" + str(total_profit_losses))
print("----------------------------")
print("Average Change: $" + str(format(average_month_change, '.2f')))
print("----------------------------")
print("Biggest Increase in Profits: " + biggest_increase_month 
      + " ($" + str(biggest_increase) + ")")
print("Biggest Decrease in Profits: " + biggest_decrease_month 
      + " ($" + str(biggest_decrease) + ")")

# Write to text file
f = open("Analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")        
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total: $" + str(total_profit_losses) + "\n")
f.write("Average Change: $" + str(format(average_month_change, '.2f')) + "\n")
f.write("Biggest Increase in Profits: " + biggest_increase_month 
      + " ($" + str(biggest_increase) + ")\n")
f.write("Biggest Decrease in Profits: " + biggest_decrease_month 
      + " ($" + str(biggest_decrease) + ")\n")
f.close()