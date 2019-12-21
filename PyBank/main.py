# import OS and CSV modules
import os
import csv
import re


# path to collect data from PyBank folder
budget_csv_path = os.path.join('..', 'PyBank', 'budget_data.csv')



# read in CSV file
with open(budget_csv_path,newline='') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csv_reader)



# create list to contain row values for months and amounts
    months = []
    amounts = []
    for row in csv_reader:
        months.append(row[0])
        amounts.append(int(row[1]))

# calculate total number of months and total amounts
        Total_months = len(months)
        Total_amounts = sum(amounts)


# create a new list to contain differences between current row and previous row
    amount_changes = []
    for i in range(1,len(months)):
        amount_changes.append(amounts[i] - amounts[i-1])


# calculate average, max, and min amounts
        average_changes = round(sum(amount_changes)/len(amount_changes),2)
        max_amount_changes = max(amount_changes)
        min_amount_changes = min(amount_changes)

        max_amount_changes_date = months[amount_changes.index(max_amount_changes)]
        min_amount_changes_date = months[amount_changes.index(min_amount_changes)]


    print("\nFinancial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {Total_months}")
    print(f"Total Amounts: ${Total_amounts}")
    print(f"Average Change: ${average_changes}")
    print(f"Greatest Increase in Profits: {max_amount_changes_date} (${max_amount_changes})")
    print(f"Greatest Decrease in Profits: {min_amount_changes_date} (${min_amount_changes})")

