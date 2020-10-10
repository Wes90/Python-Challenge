import os   
import csv
#open csv path
with open('Resources/budget_data.csv', newline= '') as file:
    csv_reader=csv.reader(file, delimiter=',')
    header=next(csv_reader)
#create variables
    total_months = 0
    months = []
    total_profit = 0
    previous_profit = 867884
    current_profit = 0
    profit_change = 0
    profit_changes = []
#create for loop, count each month    
    for row in csv_reader:
        total_months +=1
        months.append(row[0])
        total_profit += int(row[1])
        current_profit = int(row[1])
#previous profit and profit change  
        if total_months > 1:
            profit_change = current_profit - previous_profit
            profit_changes.append(profit_change) 
            previous_profit = current_profit
#maximum and minimum profit changes
net_total_profit_changes = sum(profit_changes)
average_change = round(net_total_profit_changes / (total_months - 1), 2)
max_profit_change = max(profit_changes)
min_profit_change = min(profit_changes)
max_month = months[profit_changes.index(max_profit_change) + 1]
min_month = months[profit_changes.index(min_profit_change) + 1]
#print results
lines = '------------'           
print('Finacial Analysis')
print(lines)
print(f'Total Months: {total_months}' )
print(f'Total: {total_profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_month} (${max_profit_change})')
print(f'Greatest Decrease in Profits: {min_month} (${min_profit_change}')
#export text file
with open('Output.txt', 'w') as text_file:
    text_file.write('\nFinacial Analysis')
    text_file.write('\n'+lines)
    text_file.write(f'\nTotal Months: {total_months}' )
    text_file.write(f'\nTotal: {total_profit}')
    text_file.write(f'\nAverage Change: ${average_change}')    
    text_file.write(f'\nGreatest Increase in Profits: {max_month} (${max_profit_change})')   
    text_file.write(f'\nGreatest Decrease in Profits: {min_month} (${min_profit_change}')    
   
       
        
    
    
