#sieve of Eratosthenes

n = int(input("will compute the prime numbers smaller than: "))

numbers = [True for i in range(n+1)]

for i in range(2, n//2 + 1, 1):
    if numbers[i]:
        for j in range(i + i, n, i): # "delete" all multiples
            numbers[j] = False

#print them
for i in range(1, n):
    if numbers[i]:
        print(i)
