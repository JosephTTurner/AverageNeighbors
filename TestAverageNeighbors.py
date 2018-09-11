## Test Suite for AverageNeighbors method ##

from AverageNeighbors import AverageNeighbors
from AverageNeighbors import print_matrix

print("\n----- Running correctness tests -----\n")

print("Testing 2x2 0 matrix: \n")

test_matrix_0 = [[0,0],[0,0]]

print_matrix(test_matrix_0)

aveMatrix_0 = AverageNeighbors(test_matrix_0)

print("Result: \n")
print_matrix(aveMatrix_0)

print("Testing correctness...")
for i in range(2):
	for j in range(2):
		assert(aveMatrix_0[i][j] == 0)
print("Passed!\n")

print("Testing 3x3 numeric matrix: \n")
test_matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]

print_matrix(test_matrix_1)

aveMatrix_1 = AverageNeighbors(test_matrix_1)

print("Result: \n")
print_matrix(aveMatrix_1)


print("Testing correctness...")
assert(aveMatrix_1[0][0] == sum([1,2,4,5])/4)
assert(aveMatrix_1[0][1] == sum([1,2,3,4,5,6])/6)
assert(aveMatrix_1[0][2] == sum([2,3,5,6])/4)
assert(aveMatrix_1[1][0] == sum([1,2,4,5,7,8])/6)
assert(aveMatrix_1[1][1] == sum([1,2,3,4,5,6,7,8,9])/9)
assert(aveMatrix_1[1][2] == sum([2,3,5,6,8,9])/6)
assert(aveMatrix_1[2][0] == sum([4,5,7,8])/4)
assert(aveMatrix_1[2][1] == sum([4,5,6,7,8,9])/6)
assert(aveMatrix_1[2][2] == sum([5,8,6,9])/4)
print("Passed!\n")


print("Testing 4x4 numeric matrix: \n")

testMatrix_5 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print_matrix(testMatrix_5)

aveMatrix_5 = AverageNeighbors(testMatrix_5)

print("Result: \n")

print_matrix(aveMatrix_5)

print("Testing correctness...")

assert(aveMatrix_5[0][0] == sum([1,2,5,6])/4)
assert(aveMatrix_5[0][1] == sum([1,2,3,5,6,7])/6)
assert(aveMatrix_5[0][2] == sum([2,3,4,6,7,8])/6)
assert(aveMatrix_5[0][3] == sum([3,4,7,8])/4)
assert(aveMatrix_5[1][0] == sum([1,2,5,6,9,10])/6)
assert(aveMatrix_5[1][1] == sum([1,2,3,5,6,7,9,10,11])/9)
assert(aveMatrix_5[1][2] == sum([2,3,4,6,7,8,10,11,12])/9)
assert(aveMatrix_5[1][3] == sum([3,4,7,8,11,12])/6)
assert(aveMatrix_5[2][0] == sum([5,6,9,10,13,14])/6)
assert(aveMatrix_5[2][1] == sum([5,6,7,9,10,11,13,14,15])/9)
assert(aveMatrix_5[2][2] == sum([6,7,8,10,11,12,14,15,16])/9)
assert(aveMatrix_5[2][3] == sum([7,8,11,12,15,16])/6)
assert(aveMatrix_5[3][0] == sum([9,10,13,14])/4)
assert(aveMatrix_5[3][1] == sum([9,10,11,13,14,15])/6)
assert(aveMatrix_5[3][2] == sum([10,11,12,14,15,16])/6)
assert(aveMatrix_5[3][3] == sum([11,12,15,16])/4)

print("Passed!\n")


print("\n----- Running assertion tests -----\n")

print("\nTesting garbage string as input...")

try:
	aveGarbage = AverageNeighbors("garbage")
except:
	print("Assertion error reported due to garbage input")

print("Passed!\n")

print("Testing single element matrix: \n")

print(0, "\n")

try:
	ave0 = AverageNeighbors([0])
except:
	print("Type error reported due to single element matrix:\n")


print("Passed!\n")

print("Testing single row: \n")
	
test_row = [1,2,3]

print(test_row, "\n")

try:  
	AverageNeighbors(test_row)
except:
	print("Assertion error eported due single row")

print("Passed!\n")


print("Testinge matrix containing non-numeric elements: \n")

test_matrix_2 = [['a', 'b'], [1, 2]]

print_matrix(test_matrix_2)

try:
	aveMatrix_2 = AverageNeighbors(test_matrix_2)
except:
	print("Assertion error reported due to non-numeric element")

print("Passed!\n")


print("Testing non-symmetrical matrix:\n")

test_matrix_3 = [[0,0], [0]]

print_matrix(test_matrix_3)

try:
	aveMatrix_3 = AverageNeighbors(test_matrix_3)
except:
	print("Assertion error eported due to non-symmetrical matrix\n")


print("Testing non-symmetrical matrix:\n")

test_matrix_4 = [[0], [0,0]]

print_matrix(test_matrix_4)

try:
	aveMatrix_4 = AverageNeighbors(test_matrix_4)
except:
	print("Assertion error reported due to non-symmetrical matrix")

print("Passed!\n")
