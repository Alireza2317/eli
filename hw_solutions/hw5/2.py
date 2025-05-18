def sum_mats(mat1, mat2):
	# number of rows don't match
	if len(mat1) != len(mat2):
		return None

	# number of columns don't match
	if len(mat1[0]) != len(mat2[0]):
		return None

	smat = [
		[0 for _ in range(len(mat1))]
		for _ in range(len(mat1[0]))
	]

	for row in range(len(mat1)):
		for col in range(len(mat1[0])):
			smat[row][col] = mat1[row][col] + mat2[row][col]

	return smat


A = [
	[1, 2, 6],
	[4, 3, 1],
	[0, 9, 5]
]

B = [
	[3, 2, -2],
	[1, 0, -1],
	[0, 4, 9]
]

C = sum_mats(A, B)

for row in C:
	for element in row:
		print(element, end='\t')

	print()
