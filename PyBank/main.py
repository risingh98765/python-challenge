import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

dates = []
total_months = 0
monthly_profit = []
net_profit = 0 
monthly_change = []
avg_monthly_change = 0
max_increase_profit_change = 0
max_decrease_profit_change = 0 
max_increase_month = None
max_decrease_month = None



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        total_months += 1
        monthly_profit.append(int((row[1])))
        net_profit = sum(monthly_profit)
        dates.append(row[0])
    
    
    for b in range(len(monthly_profit)-1):

        monthly_change.append(monthly_profit[b+1] - monthly_profit[b])
    avg_monthly_change = sum(monthly_change)/len(monthly_change)

    max_increase_profit_change = max(monthly_change)
    max_decrease_profit_change = min(monthly_change)
    
    
    max_increase_month = dates[monthly_change.index(max(monthly_change)) + 1]
    max_decrease_month = dates[monthly_change.index(min(monthly_change))+1]


filepath = os.path.join('Analysis','financial_analysis.txt')
with open(filepath,'w') as text:
    text.write(f'Financial Analysis')
    text.write('/n')
    text.write('----------------------------------------------------------------------------------')
    text.write('/n')
    text.write(f'Total Months: {total_months}')
    text.write('/n')
    text.write(f'Average Change {avg_monthly_change}')
    text.write('/n')
    text.write(f'Greatest Increase in Profits: {max_increase_month} ({max_increase_profit_change})')
    text.write('/n')
    text.write(f'Greatest Decrease in Profits: {max_decrease_month} ({max_decrease_profit_change})')

    


print('Financial Analysis')
print('----------------------------------------------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Average Change {avg_monthly_change}')
print(f'Greatest Increase in Profits: {max_increase_month} ({max_increase_profit_change})')
print(f'Greatest Decrease in Profits: {max_decrease_month} ({max_decrease_profit_change})')

