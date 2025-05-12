#guess an integer number between 0 and n = 100

n = 100
guess = n // 2

bigger = n
lower = 0

indication = input(f"it is {guess}? 'y' means 'yes', 's' means smaller guess, 'b' meas bigger guess: ")

while indication != 'y':
    if indication == 's':
        lower = guess
        guess = (lower + bigger) // 2
        indication = input(f"it is {guess}? 'y' means 'yes', 's' means smaller guess, 'b' meas bigger guess: ")
    elif indication  == 'b':
        bigger = guess
        guess = (lower + bigger) // 2
        indication = input(f"it is {guess}? 'y' means 'yes', 's' means smaller guess, 'b' meas bigger guess: ")
    else:
        indication = input(f"it is {guess}? 'y' means 'yes', 's' means smaller guess, 'b' meas bigger guess: ")
print(f"Finally I won! Your secret number is {guess}")        
