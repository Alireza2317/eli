A = 2
B = 6

#1
#def multiply(a, b):
#	s = 0
#	for i in range(a):
#		s += b
#	return s

#def power(a, b):
#	if b == 0:
#		return 1

#	s = multiply(a, power(a, b-1))
#	return s


#2
#def power(a, b):
#	if b == 0:
#		return 1

#	s = 0
#	for i in range(a):
#		s += power(a, b-1)

#	return s

#3
#def multiply(a, b):
#	s = 0
#	for i in range(a):
#		s += b
#	return s

#def power(a, b):
#	if b == 0:
#		return 1

#	result = a

#	for i in range(b-1):
#		result = multiply(result, a)

#	return result


#4
def power(a, b):
	if b == 0:
		return 1

	result = a

	for i in range(b-1):
		mult = 0
		for j in range(a):
			mult += result

		result = mult

	return result

print(power(A, B))