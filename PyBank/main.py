import os
import csv

# Log file address in py_bank_csv
py_bank_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Add variables
month_count = 0
total_sum = 0
prior_value = 0
difference = []

# Scan CSV file
with open(py_bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip header row
    next(csvreader)
    for row in csvreader:
        # Count months
        month_count += 1
        # Sum profit/loss
        total_sum += int(row[1])
        # Substract new vs old to get difference
        new_vs_old = int(row[1]) - prior_value
        # Include new column with the diff
        difference.append(new_vs_old)
        # Set the prior profit as the current one
        prior_value = int(row[1])
        
# Calculate average change in profit/losses
avg_delta = sum(difference) / len(difference)

# Calculate greatest increase in profit and corresponding date
biggest_growth = max(difference)

# Calculate greatest decrease in profit and corresponding date
biggest_reduction = min(difference)

# Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_sum}")
print(f"Average Change: ${round(avg_delta, 2)}")
print(f"Greatest Increase: ${biggest_growth}")
print(f"Greatest Decrease: ${biggest_reduction}")

# data rows as dictionary objects 
mydict =[{'Total Months': month_count}, 
         {'Total': total_sum}, 
         {'Average Change': avg_delta},
         {'Greatest Increase': biggest_growth},
         {'Greatest Decrease': biggest_reduction},]

#Create file
with open('Analysis.txt','w') as f:
    f.write('Financial Analysis')
    f.write('\n')
    f.write('-------------------------------------------')
    f.write('\n')
    f.write('Total months: ')
    f.write(str(month_count))
    f.write('\n')
    f.write('Total: ')
    f.write(str(total_sum))
    f.write('\n')
    f.write('Average Change: $')
    f.write(str(avg_delta))
    f.write('\n')
    f.write('Greatest Increase: ')
    f.write(str(biggest_growth))
    f.write('\n')
    f.write('Greatest Decrease: ')
    f.write(str(biggest_reduction))
    f.write('\n')