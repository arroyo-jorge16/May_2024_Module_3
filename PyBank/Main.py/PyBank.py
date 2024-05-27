
# Import dataset
import csv
csvpath = "C:/Users/Jorge/OneDrive/Desktop/DSBootCamp/homework/ds_may2024_module_3_Python/May_2024_Module_3/PyBank/resources/budget_data.csv"

# Find the total number of months in the dataset

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    next_row = next(csvreader)
    
    month_count = 0
    profit_loss_total = 0

    # I got help from Reed for month count
    for row in csvreader:
        month_count = month_count + 1
        # The net total amount of "Profit/Losses" over the entire period
        months = row[0]
        profit_loss_total = profit_loss_total + int(row[1])
           
    print("total months:", int(month_count))
    print("Profit/Loss total:", profit_loss_total) 
    
        
    

    # The net total amount of "Profit/Losses" over the entire period
      


    #  The changes in "Profit/Losses" over the entire period, and then the average of those changes
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    next_row = next(csvreader)
    
    
    

    months = 0
    current_net = 0
    previous_net = 0
    total_difference = 0
    average_change = 0
    row_num = 0
    maximum_profit = 0
    minimum_profit = 0 
    greatest_inc_row = ''
    greatest_dec_row = ''

    for current_row in csvreader: 
        
        if row_num == 0:
            previous_net = int(current_row[1])
            row_num += 1
            continue

        current_net = int(current_row[1])
        current_difference = (current_net - previous_net) 
        previous_net = current_net
        total_difference += current_difference
        average_change += 1
    
        if maximum_profit < current_difference:
            maximum_profit = current_difference 
            greatest_inc_row = current_row[0]
        
        if minimum_profit > current_difference:
            minimum_profit = current_difference
            greatest_dec_row = current_row[0]
        
            
        # if average_change > 75:
        #     print(current_difference)
        # previous_difference = current_difference
        next
    
      
            
        
    # total_difference = current_difference/len(csvreader)
    print ("Average Change:", total_difference/(average_change))
    print("Greatest increase in profits:", greatest_inc_row, maximum_profit)
    print("Greatest decrease in profits:", greatest_dec_row, minimum_profit)

   

    

# # The greatest increase in profits (date and amount) over the entire period



# # The greatest decrease in profits (date and amount) over the entire period