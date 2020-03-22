# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period
import os
import csv

budget_data_csv_path = os.path.join(".", "Resources", "budget_data.csv")

total_months = []
total_profit = []
profit_change = []

with open(budget_data_csv_path) as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")

     # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)       
    # Read through each row of data after the header
    # The total number of months included in the dataset
    for row in csv_reader:
        total_months.append(row[0])

# The net total amount of "Profit/Losses" over the entire period
        total_profit.append(int(row[1]))

# The average of the changes in "Profit/Losses" over the entire period
for i in range(len(total_profit)-1):
        difference = (total_profit[i] - total_profit[i+1])
        profit_change.append(difference)

average_change = sum(profit_change)/len(profit_change)

# The greatest increase in profits (date and amount) over the entire period
max_profits = max(total_profit)
max_profits_month = total_months[total_profit.index(max(total_profit))]

# The greatest decrease in losses (date and amount) over the entire period
min_profits = min(total_profit)
min_profits_month = total_months[total_profit.index(min(total_profit))]

#Print summary of results to the terminal
print("Financial Analysis")
print("-"*25)
print(f"Total Number of Months: {len(total_months)}")
print(f"Total Amount of Profit/Losses: ${sum(total_profit)}")
print(f"Average of the Profit/Losses: ${round((average_change),2)}")
print(f"Greatest increase in profits: {(max_profits_month)} (${(max_profits)})")
print(f"Greatest decrease in losses: {(min_profits_month)} (${(min_profits)})")

#Print summary of results in a text file.\n seperates each line
text_file = open("budget_summary_output.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("-"*25)
text_file.write(f"\nTotal Number of Months: {len(total_months)}\n")
text_file.write(f"Total Amount of Profit/Losses: ${sum(total_profit)}\n")
text_file.write(f"Average of the Profit/Losses: ${round((average_change),2)}\n")
text_file.write(f"Greatest increase in profits: {(max_profits_month)} (${(max_profits)})\n")
text_file.write(f"Greatest decrease in losses: {(min_profits_month)} (${(min_profits)})\n")
text_file.close()