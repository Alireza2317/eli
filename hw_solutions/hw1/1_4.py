N = 7

#1
prime_numbers = []
number = 2
is_prime = True

while len(prime_numbers) < N:
	is_prime = True
	for i in range(2, number):
		if number%i == 0:
			is_prime = False
			break

	if is_prime:
		prime_numbers.append(number)

	number += 1

print(prime_numbers)


#2
#prime_numbers = []
#number = 2

#while len(prime_numbers) < N:
#	for i in range(2, number):
#		if number%i == 0:
#			break
#	else:
#		prime_numbers.append(number)

#	number += 1

#print(prime_numbers)


#3
#def is_prime(n):
#	for i in range(2, n):
#		if n%i == 0:
#			return False

#	return True


#prime_numbers = []
#number = 2
#while len(prime_numbers) < N:
#	if is_prime(number):
#		prime_numbers.append(number)

#	number += 1

#print(prime_numbers)

for prime in prime_numbers:
	print(prime)