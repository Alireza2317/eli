A = 'hello'

while A:
	c = input('Enter a character: ')
	A = A.replace(c, '')
	print(A)