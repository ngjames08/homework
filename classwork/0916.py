#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#Hints:
#Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
#siavash mortezavi [5:55 PM]
#Bonus:
#Write a program which takes 3 digits, X,Y,Z as input and generates a 3-dimensional array. The element value in the i,j,k can be anything you like.
#Suppose the following inputs are given to the program:
#2,2,3
#Then, the output of the program should be:
#array( [ [ [2., 1., 0.], [2., 1., 0.] ], [ [2., 1., 0.], [2., 1., 0.] ] ] )

def matrix_maker(rows,cols):
	matrix = []
	for row in range(rows):
		elements = []
		for col in range(cols):
			elements.append(elements)
		return matrix

my_input = input('Please enter two digits separated by a comma like this: 2,3: ')
dimensions = [int(item) for item in my_input.split(',')]
rows, cols = dimensions
matrix_maker(rows,cols)
print(matrix_maker)
