import csv
import os
# Define the file path

data_path = os.path.join("Resources","election_data.csv")


# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(data_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Extract candidate name from the row
        candidate_name = row[2]

        # Update candidate's votes count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1


# write File

report_path = "election_report.txt"

writeFile = open(report_path,"w")

writeFile.write("Election Results\n")
writeFile.write("-------------------------\n")
writeFile.write(f"Total Votes: {total_votes}\n")
writeFile.write("-------------------------\n")

# Calculate and print the percentage and total votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    writeFile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    # Check for the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
# Print the winner
writeFile.write("-------------------------\n")
writeFile.write(f"Winner: {winner}\n")
writeFile.write("-------------------------\n")
writeFile.close()


# Read File in console
readFile = open(report_path,"r")
report = readFile.read()
print(report)
readFile.close()
