import os
import csv

# Define the variables
months = []  
change_list = []
total_change = 0
total_month = 1
total_amount= 0
greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999]

# Read using csv module
fpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv") 

# Get data from the csv file
with open (fpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    next(csvreader)

    first_row = next(csvreader)
    previous_value = int(first_row[1])
    total_amount = int(first_row[1])
    
    # Loop through the csv file
    for row in csvreader:

        total_amount +=int(row[1])
        total_month += 1
        current_value = int(row[1])
        
        change_value = int(current_value-previous_value)

        change_list.append(change_value)
        months.append(row[0])
        previous_value = int(row[1])

        total_change += change_value 
        if change_value > greatest_increase[1]:
           greatest_increase[0] = str(row[0])
           greatest_increase[1] = change_value


        if change_value < greatest_decrease[1]:
           greatest_decrease[0] = str(row[0])
           greatest_decrease[1] = change_value
		
        # Calculate the average change
        average_change = total_change/len(months)

# Output summary 
output = (
   f"\nFinancial Analysis\n"
   f"--------------------------------\n"
   f"Total Months: {total_month}\n"
   f"Total: ${total_amount}\n"
   f"Average  Change: ${average_change:.2f}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print output to terminal
print(output)

# Output path
analysis = os.path.join("..", "PyBank", "Analysis_PyBank", "Analysis.txt")

# Export an analysis text
with open(analysis, "w") as txt_file:
   txt_file.write(output)  

   analysis