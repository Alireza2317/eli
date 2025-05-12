string = '32563241'

def print_histogram(string):
	for digit in range(10):
		c = string.count(str(digit))
		print(f'{digit}:{c * "*"}')

print_histogram(string)