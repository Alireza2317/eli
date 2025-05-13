N = 4

def print_tree(n):
	for i in range(1, n):
		print(' ' + i*'*')

	print((n+1) * '*')

	for i in range(n-1, 0, -1):
		print(' ' + i*'*')

print_tree(N)