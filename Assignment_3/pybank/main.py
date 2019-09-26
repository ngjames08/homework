#import file
import csv
#import mean 
import numpy as np 
#open file
with open('budget_data.csv') as csvfile:
	data_file = csv.reader(csvfile, delimiter=",")
	month_count = 0
	profit = []
	difference = []
	month = []
	headers = next(data_file)
# to get the month count
	for row in data_file:
		month_count = month_count + 1 	
		profit.append(float(row[1]))
		month.append(row[0])
	sum1 = 0
# to get the net profit
	for item in profit:
		sum1 = item + sum1
	average1 = 0	
# to get the mean of profit 
	for delta in range(1,len(profit)):
		changes1 = profit[delta] - profit[delta -1]
		difference.append(changes1)
	average1 = np.mean(difference)

	max_value = 0
	for num in difference:
		if num > max_value:
			max_value = num
		else:
			continue

	min_value = 0
	for num in difference:
		if num < min_value:
			min_value = num
		else:
			continue

	max_index = difference.index(max_value)
	max_month = month[max_index + 1]
	min_index = difference.index(min_value)
	min_month = month[min_index + 1]

	#for monthvalue, maxvalue in difference:
		#max(difference)
	#for minvalue1 in difference:
		#min(difference)

	print(sum1)
	print(month_count)
	print(average1)
	print(max_value)
	print(max_month)
	print(min_value)
	print(min_month)


	
