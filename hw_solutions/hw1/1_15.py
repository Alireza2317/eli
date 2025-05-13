string = '3 54 23 11 678 43 23 22'

#1
#numbers = string.split()
#numbers = [int(n) for n in numbers]
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers) / len(numbers))


#2
numbers_str = string.split()
numbers = []
for ns in numbers_str:
	numbers.append(int(ns))


minimum = numbers[0]
maximum = numbers[0]
addition = 0

for number in numbers:
	addition += number

	if number > maximum:
		maximum = number

	if number < minimum:
		minimum = number

average = addition / len(numbers)

print(minimum)
print(maximum)
print(average)