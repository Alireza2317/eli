N = int(input('Finding primes less than? '))

numbers = [True for _ in range(1, N+1)]

for i in range(len(numbers)):
	if numbers[i]:
		for d in range(i, N+1, i):
			numbers[d] = False

for i, f in enumerate(numbers):
	if f:
		print(i+1)
