# 1000th prime number which has a 7 in the one's place
# and the sum of its digits exceed 23
from math import ceil, sqrt


def sum_digits(number):
	s = 0
	num_str = str(number)
	for d in num_str:
		s += int(d)

	return s

def is_prime(number):
	if number == 1:	return False
	if number == 2:	return True

	for i in range(2, ceil(sqrt(number))+1):
		if number%i == 0:
			return False

	return True

def is_last_digit_7(number):
	return (number%10) == 7


counter = 0
number = 2
while True:
	if (
		is_prime(number) and
		is_last_digit_7(number) and
		sum_digits(number) > 23
	):
		counter += 1

	if counter == 1000:
		print(number)
		break
	number += 1