A = 27
B = 13

# least common multiple ک م م
# greatest common divisor ب م م

A_divisors = []
B_divisors = []

for a in range(1, A+1):
	if A%a == 0:
		A_divisors.append(a)

for b in range(1, B+1):
	if B%b == 0:
		B_divisors.append(b)

A_divisors = set(A_divisors)
B_divisors = set(B_divisors)

common = A_divisors.intersection(B_divisors)
gcd = max(common)
lcm = A*B // gcd

print(gcd)
print(lcm)