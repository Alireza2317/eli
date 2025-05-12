number = 1234

def count_digits(number):
	num_digits = 0
	while number:
		num_digits += 1
		number //= 10

	return num_digits

print(count_digits(number))