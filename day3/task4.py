#Take a 3x3 matrix written as a list of lists. Write code that prints its transpose (rows become columns) using a nested list comprehension.
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
print("\n")