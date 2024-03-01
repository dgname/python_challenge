import os
import csv

budgetdata_csv = os.path.join("Resources", "budget_data.csv")

with open(budgetdata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next (csvreader) #Skip the header

    rows_with_date = 0 #initial variable value
    sum_profits_losses = 0
    previous_profit_losses = None
    variances = [] # differences in profits/losses will be stored in a list4

    for row in csvreader: #iterate through all rows (except header which we already excluded)
        date = row[0]
        if date: #checks if date has a value
            rows_with_date += 1

        changes_in_money = int(row[1])
        sum_profits_losses += changes_in_money

        if previous_profit_losses is not None:
            variance = changes_in_money - previous_profit_losses
            variances.append((variance,date))

        previous_profit_losses = changes_in_money


average_variance = "{:.2f}".format(sum(variance for variance, _ in variances) / len(variances) if variance else 0)
highest_increase, highest_increase_date = max(variances,default=(0, None))
highest_decrease, highest_decrease_Date = min(variances,default=(0, None))

print("Total Months:",rows_with_date)
print("Total:",sum_profits_losses)
print("Average Change:",average_variance)
#print("variances for each row:", variances)
print("Greatest Increase in Profits:", highest_increase_date, "(" ,highest_increase,")")
print("Greatest Decrease in Profits:", highest_decrease_Date, "(", highest_decrease, ")")

# Export analysys to a text file

output_file = "financial_analysis.txt"
with open(output_file,"w") as text_file:
    text_file.write("Financial Analysis\n") # the \n is used to input a new line (space)
    text_file.write("--------------------------\n")
    text_file.write(f"Total Months: {rows_with_date}\n")
    text_file.write(f"Total: {sum_profits_losses}\n")
    text_file.write(f"Average Change: {average_variance}\n")
    text_file.write(f"Greatest Increase in Profits: {highest_increase_date}  (Date: {highest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {highest_decrease_Date}  (Date: {highest_decrease})\n")

