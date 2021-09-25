# Import the NumPy library
import numpy as np
# Import the NumPy Financial library
import numpy_financial as npf
# Import from the pathlib library, the main class Path
from pathlib import Path
import pandas as pd
import os
import csv
# Import statistics Library
import statistics
# Check the current directory where the Python program is executing from
# print(f"Current Working Directory: {Path.cwd()}")
# Set the path normally (Windows)
# Set string raw literal due to backslashes acting as escape characters for
# the Windows 
file = r'./Resources/budget_data.csv'

# Read the file without a header
budget_data = pd.read_csv(file)
budget_data.head()
# use Pandas dataframe, shape[0] gives number of rowcount, shape[1] gives number of column count
#budget_data.describe()
count_row=budget_data.shape[0]
#subtract the header row to get total count of month
total_month=count_row
print(f"Total Months:{total_month} ")
#*******************#
csvpath = os.path.join(".", "Resources", "budget_data.csv")
# Create new lists to store data for heaviest and tallest pokemon
profit_loss = []
total = 0   

# Open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip the first row: column name
    csv_header = next(csvreader)
    for row in csvreader:
        #convert str into float data ty
        profit_loss.append(float(row[1]))
        total=total+float(row[1])
print(f"Total: ${total}")

#create a list to store the budget difference between current and previous month 
profit_loss_change = []
pointer=1
for x in profit_loss:
    if pointer < len(profit_loss):
        profit_loss_change.append(profit_loss[pointer]-profit_loss[pointer-1])
        pointer+=1
#print(profit_loss_change)
print(f"Average change:","${:.2f}".format(statistics.mean(profit_loss_change)))


# =============================================================================
# 4. The greatest increase in profits (date and amount) over the entire period.
#Prepend the budget difference for the first month as '0'
profit_loss_change.insert(0,0)
#Assign the budget different from the list to the dataframe
budget_data["Changes"] =profit_loss_change
budget_data.head()

# Set the index as the 'Date' column
greatest_increase = max(profit_loss_change)
budget_data.set_index(budget_data['Changes'], inplace=True)
budget_data.head()
#use loc as dictionary to check dataframe to find month
greatest_month=budget_data.loc[greatest_increase]["Date"]
print(f"Greatest Increase in Profits:{greatest_month} (${greatest_increase})" )

# =============================================================================
# =============================================================================
# 5. The greatest decrease in losses (date and amount) over the entire period.
greatest_decrease =min(profit_loss_change)
#use loc as dictionary to check dataframeto find month
worst_month=budget_data.loc[greatest_decrease]["Date"]
print(f"Greatest Decrease in Profits::{worst_month} (${greatest_decrease})" )

# =============================================================================



