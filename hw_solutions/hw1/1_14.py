A = 'hello'
B = 'world'
p = 2

if p >= len(B):
	output = B
else:
	output = B[:p] + A + B[p:]

print(output)