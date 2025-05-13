N = int(input('Finding primes less than? '))

numbers = [True for _ in range(N)]

for i in range(2, N):
	if numbers[i]:
		for d in range(2*i, N, i):
			numbers[d] = False

for i in range(2, N):
	if numbers[i]:
		print(i)
