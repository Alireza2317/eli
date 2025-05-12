# Output the number of parking spaces that were occupied on both days.

yesterday = input().split()
today = input().split()

counter = 0

#for y, t in zip(yesterday, today):
#	if y == t and y == 'C':
#		counter += 1

for i in range(len(yesterday)):
	if yesterday[i] == today[i] and today[i] == 'C':
		counter += 1

print(counter)