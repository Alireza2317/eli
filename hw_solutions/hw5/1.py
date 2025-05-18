def create_matrix(n):
	matrix = [
		[0 for _ in range(n)]
		for _ in range(n)
	]

	for row in range(n):
		for col in range(n):
			matrix[row][col] = (row+1) * (col+1)

	return matrix

for row in create_matrix(4):
	for element in row:
		print(element, end='\t')

	print()