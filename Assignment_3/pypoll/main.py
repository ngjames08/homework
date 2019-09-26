#import file
import csv
#import mean 
import numpy as np 
import operator
#open file
with open('election_data.csv') as csvfile:
	data_file = csv.reader(csvfile, delimiter=",")
	vote_count = 0
	candidate_count = 0
	county = []
	candidate1 = 0
	candidate2 = 0
	candidate3 = 0
	candidate4 = 0
	headers = next(data_file)
# to get the total vote cast and count the candidates
	for candidate in data_file:
		vote_count = vote_count + 1 
		if candidate[2] == "Khan":
			candidate1 = candidate1 + 1
		elif candidate[2] == "Correy":
			candidate2 = candidate2 + 1
		elif candidate[2] == "Li":
			candidate3 = candidate3 + 1
		else :
			candidate4 = candidate4 +1 	
# to get the percentages
percentage1 = ((candidate1/vote_count) * 100)
percentage2 = ((candidate2/vote_count) * 100)
percentage3 = ((candidate3/vote_count) * 100)
percentage4 = ((candidate4/vote_count) * 100)
# print the output 
print("Total Votes:",vote_count)
print("Khan: ", round(percentage1,3),"%", candidate1)
print("Correy: ", round(percentage2,3),"%", candidate2)
print("Li: ", round(percentage3,3),"%",candidate3)
print("O'Tooley: ", round(percentage4,3),"%", candidate4)
#create a dictionary and find the winner:
# Reference: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

import operator
x = {
	'Khan':candidate1,
	'Correy': candidate2,
	'Li':	candidate3,
	'O Tooley': candidate4
}
winner = max(x.items(),key=operator.itemgetter(1))[0]
print("The Winner is :", winner)