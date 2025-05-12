MAX = 1000
MIN = 0
print(f'Choose a number between {MIN} and {MAX-1}. I will guess it!')

guess = (MAX-MIN) // 2

while True:
	print(f'is it {guess}?')
	print("type 'y' for yes (correct guess) ")
	print("type 's' if your number is smaller")
	print("type 'b' if your number is bigger")
	command = input('>>> ')

	if command == 'y':
		print(f'Your number was {guess}! yay!')
		break

	if command not in 'sb':
		print('invalid input!')
		continue

	if command == 'b':
		MIN = guess
	elif command == 's':
		MAX = guess

	guess = (MAX + MIN) // 2

