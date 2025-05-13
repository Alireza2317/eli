
































#def floyd(n):
#	number = 1
#	for row in range(1, n+1):
#		nums_in_row = []
#		for _ in range(row):
#			nums_in_row.append(number)
#			number += 1

#		print(row, tuple(nums_in_row))


#def floyd2(n):
#	number = 1
#	for row in range(1, n+1):
#		t = tuple(range(number, number+row))
#		number += row
#		print(row, t)

#floyd2(5)