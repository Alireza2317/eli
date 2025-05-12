def is_prime(number):
	for i in range(2, number):
		if number % i == 0:
			return False
	return True



for number in range(2, 20):
	if is_prime(number):
		print(number)
