A = 27
B = 13

# least common multiple ک م م
# greatest common divisor ب م م


# greatest common divisor
#1
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



# greatest common divisor
#2
#smaller = A if A < B else B

if A < B:
	smaller = A
else:
	smaller = B

gcd = smaller
while True:
	if (A%gcd == 0) and (B%gcd == 0):
		break
	gcd -= 1


lcm = A*B // gcd

print(gcd)
print(lcm)