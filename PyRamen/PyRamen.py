# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
# Initial imports
import pandas as pd
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('./Resources/menu_data.csv')
sales_filepath = Path('./Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
#Use a with statement and open the menu_data.csv by using its file path.
#Use the reader function from the csv library to begin reading menu_data.csv.
with open(menu_filepath) as menu_file:
    # Store all of the text from the file inside a variable called "text"
    # and print the contexts of the text file
    csvreader = csv.reader(menu_file, delimiter=",")
    # skip the first row: column name
    csv_header = next(csvreader)
    for row in csvreader:     
#Loop over the rest of the rows and append every row to the menu list object (the outcome will be a list of lists)
        menu.append(row)

print(menu) 


# =============================================================================
# Set up the same process to read in sales_data.csv. 
#However, instead append every row of the sales data to a new sales list object.
# @TODO: Read in the sales data into the sales list
# Use the reader function from the csv library to begin reading menu_data.csv
# =============================================================================
with open(sales_filepath) as sales_file:
    csvreader = csv.reader(sales_file, delimiter=",")
    csv_header=next(csvreader)
    for row in csvreader:
        sales.append(row)
#print(sales)

Quantity = 0
Price=0
Cost=0
Menu_Item= ''

# @TODO: Initialize dict objectn [report] to hold our key-value pairs of items and metrics
report = {}
for Menu_Item in menu:    
    #print(Menu_Item[0])

    Price=Menu_Item[3]
    Cost=Menu_Item[4]
    
# @TODO: Loop over every row in the sales list object
for record in sales:
    Quantity =  int(record[3])
    Menu_Item = record[4]
    for item_master in menu:
        if Menu_Item != item_master[0]:
            report[Menu_Item]={"01-count": 0,"02-revenue": 0,"03-cogs": 0,"04-profit": 0}
            
for record in sales:  
    Quantity =  int(record[3])
    Menu_Item = record[4]
    for item_master in menu:  
        Price = float(item_master[3])
        Cost = float(item_master[4])
        Profit = float(item_master[3]) - float(item_master[4])
        if Menu_Item == item_master[0]:
            report[Menu_Item]["01-count"] += Quantity
            report[Menu_Item]["02-revenue"] += Price * Quantity
            report[Menu_Item]["03-cogs"] += Cost * Quantity
            report[Menu_Item]["04-profit"] += Profit* Quantity
        # else:
        #     print(f"{Menu_Item} does not equal {item_master[0]}! NO MATCH!")
            
# @TODO: Write out report to a text file (won't appear on the command line output)
# Set the output file path
output_path = Path("./Sales_Report.txt")
# Open the output_path as a file object in "write" mode ('w')
# Write a header line and write the contents of 'text' to the file
with open(output_path, 'w') as file:
    file.write("This is an output file.\n")
    for text in report:
        file.write(f"{text} {report[text]} \n")
# for text in report:
#     print(text, report[text])
    
    



    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit








    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
# Set the output file path
# output_path = Path("./Sales_Report.txt")
# # Open the output_path as a file object in "write" mode ('w')
# # Write a header line and write the contents of 'text' to the file
# with open(output_path, 'w') as file:
#     file.write("This is an output file.\n")
#     file.write(report)
