import csv
import os

# variables
totalMonth = 0
total = 0
previous_profit_loss = 0
changes = []
dates = []

#path

csv_path = os.path.join("Resources","budget_data.csv")
export_path = os.path.join('export_report.txt')


with open(csv_path, newline='') as file:
    csv_reader = csv.reader(file, delimiter=",")

    #skip header
    next(csv_reader)

    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])

        # total month
        totalMonth += 1
        # total
        total += profit_loss

        #calculate changes in loop
        if totalMonth>1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
        #update previous profit_loss to next loop
        previous_profit_loss = profit_loss


# average change calculation
average = sum(changes)/len(changes)

# greatestIncrease
greatestIncrease = max(changes)
greatestIncreaseIndex = changes.index(greatestIncrease) # same index
greatestIncreaseDate = dates[greatestIncreaseIndex]     # same index

# greatestDecrease
greatestDecrease = min(changes)
greatestDecreaseIndex = changes.index(greatestDecrease)
greatestDecreaseDate = dates[greatestDecreaseIndex]



# Export/Write File in txt
writeFile = open(export_path,"w")

writeFile.write("Financial Analysis\n")
writeFile.write("----------------------------\n")
writeFile.write(f"Total Months: {totalMonth}\n")
writeFile.write(f"Total: ${total}\n")
writeFile.write(f"Average Change: ${average:.2f}\n")
writeFile.write(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})\n")
writeFile.write(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})\n")

writeFile.close()

# Result in console
readFile = open(export_path,"r")
report = readFile.read()
print(report)
readFile.close()


#variable: totalMonth = 0, total = 0, changes = [], previous_profit=0, greatestIncrease = 0 

# Financial Analysis
# ----------------------------
#                                                    --create all necessary variable for column : date = row[0]
# Total Months: 86                                   --for loop , totalMonth =0, totalMonth+=1
# Total: $22564198                                   --for loop , profit = row[2], total += profit
# Average Change: $-8311.11         
#                                                    --for loop
#                                                    --if totalMonth>1:
#                                                    -- change = profit - previous_profit
#                                                    -- changes.append(change)
#                                                    -- dates.append(date)
#                                                    --previous_profit = profit  , next loop

#                                                    calculation:
#                                                    --average = sum(changes) / len(changes)
                                                    
# Greatest Increase in Profits: Aug-16 ($1862002)
#                                                    greatestIncrease = max(changes)
#                                                    greatestIncreaseIndex = changes.index(greatestIncrease)    -- same index
#                                                    greatestIncreaseDate = dates[greatestIncreaseIndex]        -- same index
#                                                    
# Greatest Decrease in Profits: Feb-14 ($-1825558)
#                                                    greatestDecrease = min(changes)
#                                                    greatestDecreaseIndex = changes.index(greatestDecrease)    -- same index
#                                                    greatestDecreaseDate = dates[greatestDecreaseIndex]        -- same index
    

# export file
# print file