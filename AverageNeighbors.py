## Python implementation of AverageNeighbors ## 

#	This method receives a 2D array (matrix) of numbers. 

#	It returns another 2D array of numbers such that
#	each element in the new matrix is to it's respective
#	element on the original matrix the average of that
#	original element and its neighbors. 

#	Neighbors include elements that are horizontally,
#	virtically, and diagonally adjacent to the current
#	element.

#	EXPECTED INPUT:
#	Symmetrical 2D array with dimensions n x m,
#	where n, m > 1

#	Single element arrays and single row arrays will report an error 
#	Non-symmetric arrays will report an error 
#	Arrays containing non-numeric elements will report an error 
#	Non-list objects will report an error

from numbers import Number

def print_matrix(matrix):
	for row in matrix:
		for element in row:
			if(isinstance(element, Number)):
				print('%5s' % element, end = ' ')
			else:
				print('%5s' % element, end = ' ')
		print()
	print()

def AverageNeighbors(matrix):

	# check that the input is the expected type...
	assert(isinstance(matrix, list), "input must be 2D array of numbers") # matrix should be a list
	assert(isinstance(matrix[0], list), "input must be 2D array of numbers") # each element in matrix list should be another list

	# and format...
	n = len(matrix)
	m = len(matrix[0])

	for row in matrix:
		assert(len(row) == m) # check for symmetry 
		for element in row:
			assert(isinstance(element, Number), "input must be 2D array of numbers") # check for non-numerics


	# initialize new matrix
	aveMatrix = [[0 for i in range (n)] for j in range(m)]

	# predefined loop iterables 
	currentSum = 0
	numNeighbors = 1	# current element will always be included

	# cycle through elements in matrices
	for i in range(n):
		for j in range(m):

			# reset number of neighbors
			numNeighbors = 1
			
			# only current element in sum
			currentSum = matrix[i][j]

			# print(matrix[i][j], end = "+ ")

			# sum existing neighbors

			if j-1 >= 0:	# left
				
				numNeighbors = numNeighbors + 1
				currentSum = currentSum + matrix[i][j-1]


				# print(matrix[i][j-1], end = "+ ")

				if i-1 >= 0: 	# upper left

					numNeighbors = numNeighbors + 1
					currentSum = currentSum + matrix[i-1][j-1]
					# print(matrix[i-1][j-1], end = "+ ")

				if i+1 < n:		# lower left

					numNeighbors = numNeighbors + 1
					currentSum = currentSum + matrix[i+1][j-1]
					# print(matrix[i+1][j-1], end = "+ ")

			if j+1 < m:		# right

				numNeighbors = numNeighbors + 1
				currentSum = currentSum + matrix[i][j+1]
				# print(matrix[i][j+1], end = "+ ")

				if i-1 >= 0: 	# upper right

					numNeighbors = numNeighbors + 1
					currentSum = currentSum + matrix[i-1][j+1]
					# print(matrix[i-1][j+1], end = "+ ")

				if i+1 < n: 	# lower right

					numNeighbors = numNeighbors + 1
					currentSum = currentSum + matrix[i+1][j+1]
					# print(matrix[i+1][j+1], end = "+ ")

			if i-1 >= 0:	# upper

				numNeighbors = numNeighbors + 1
				currentSum = currentSum + matrix[i-1][j]
				# print(matrix[i-1][j], end = "+ ")

			if i+1 < n:		# lower

				numNeighbors = numNeighbors + 1
				currentSum = currentSum + matrix[i+1][j]
				# print(matrix[i+1][j], end = "= ")

			# print(currentSum)

			aveMatrix[i][j] = currentSum / numNeighbors

			# print(currentSum, numNeighbors)

	return aveMatrix
