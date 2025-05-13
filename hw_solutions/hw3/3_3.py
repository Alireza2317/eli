tup = (('a', 13),('b', 22),('c', 30))

def func(t):
	maximum = -1
	max_str = ''
	summation = 0

	for string, num in t:
		summation += num

		if num > maximum:
			maximum = num
			max_str = string

	avg = summation / len(t)
	return (avg, maximum, max_str)


print(func(tup))