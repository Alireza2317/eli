numbers = [2, 90, 1, -7, 3.44, 5, 10, 1]

numbers += [0, 0]
#[2, 90, 1, -7, 3.44, 5, 10, 1, 0, 0]


x = numbers.pop()

print(numbers, x)
#[2, 90, 1, -7, 3.44, 5, 10, 1, 0] 0


numbers.remove(1)

print(numbers)
#[2, 90, -7, 3.44, 5, 10, 1, 0]
# Removes first occurrence of value.

numbers.sort()
print(numbers)
#[-7, 0, 1, 2, 3.44, 5, 10, 90]

numbers.sort(reverse=True)
print(numbers)
#[90, 10, 5, 3.44, 2, 1, 0, -7]


if 70 not in numbers:
	print('no 70 in list.')

if 5 in numbers:
	print('found 5 in list.')
