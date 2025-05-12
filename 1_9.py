A = 'pippo'
B = 'p'

substr = 2*B
#substr = B + B
#substr = f'{B}{B}'

#1
#counter = 0

#i = 0
#while i < len(A):
#	if substr == A[i:i+2]:
#		counter += 1

#	i += 1

#print(counter)

#2
splits = A.split(substr)
print(len(splits) - 1)