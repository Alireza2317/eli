A = '5998355'

#1
#while A:
#	maximum = 0
#	for digit in A:
#		if int(digit) > int(maximum):
#			maximum = digit

#	print(f'max={maximum} in "{A}"')

#	A = A.replace(maximum, '')


#2
def find_max(string_of_digits):
	maximum = '0'
	for digit in string_of_digits:
		if int(digit) > int(maximum):
			maximum = digit

	return maximum

while A:
	maximum = find_max(A)

	print(f'max={maximum} in "{A}"')

	A = A.replace(maximum, '')