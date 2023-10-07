import os
import csv

# Set the path to the CSV file
csv_path = os.path.join("D:\ONLINE\Excel\Starter_Code (4)\Starter_Code\PyBank\Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)
    
    for row in csvreader:
        # Update total months and net total
        total_months += 1
        net_total += int(row[1])
        
        # Calculate the change in profit
        profit_change = int(row[1]) - previous_profit
        change_list.append(profit_change)
        
        # Update greatest increase and decrease
        if profit_change > greatest_increase[1]:
            greatest_increase = [row[0], profit_change]
        if profit_change < greatest_decrease[1]:
            greatest_decrease = [row[0], profit_change]
        
        # Update previous profit
        previous_profit = int(row[1])

# Calculate the average change
average_change = round(sum(change_list) / (total_months - 1), 2)

# Generate the analysis results
analysis_results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the results to the terminal
print(analysis_results)

# Raw string literal for the file path
output_file_path = r"D:\ONLINE\Excel\Starter_Code (4)\Starter_Code\PyBank\analysis\pybank_analysis.txt"

# Now, write to the output file
with open(output_file_path, "w") as textfile:
    textfile.write(analysis_results)



##########
##########

# Set the path to the CSV file
csv_path = os.path.join("D:\ONLINE\Excel\Starter_Code (4)\Starter_Code\PyPoll\Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}
winner = ""
max_votes = 0

# Read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)
    
    for row in csvreader:
        # Update total votes
        total_votes += 1
        
        # Count votes for each candidate
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Generate the analysis results
analysis_results = "Election Results\n" + "-" * 25 + "\n"
analysis_results += f"Total Votes: {total_votes}\n" + "-" * 25 + "\n"

for candidate, votes in candidate_votes.items():
    # Calculate the percentage of votes each candidate won
    percentage = (votes / total_votes) * 100
    
    # Update the winner if necessary
    if votes > max_votes:
        winner = candidate
        max_votes = votes
    
    analysis_results += f"{candidate}: {percentage:.3f}% ({votes})\n"

analysis_results += "-" * 25 + "\n"
analysis_results += f"Winner: {winner}\n"
analysis_results += "-" * 25 + "\n"

# Print the results to the terminal
print(analysis_results)


# Raw string literal for the file path
output_file_path = r"D:\ONLINE\Excel\Starter_Code (4)\Starter_Code\PyPoll\analysis\pypoll_analysis.txt"

# Now, write to the output file
with open(output_file_path, "w") as textfile:
    textfile.write(analysis_results)