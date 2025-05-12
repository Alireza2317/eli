#ex9.py
#how to concatenate if statements

print("give me 3 integers and I will choose the biggest of them")
a = int(input("give me the first integer "))
b = int(input("give me the second integer "))
c = int(input("give me the third integer "))

if a >= b and a >= c:
	print(f"the biggest between {a}, {b}, {c} is {a}")

elif b >= a and b >= c:
	print(f"the biggest between {a}, {b}, {c} is {b}")

elif c >= a and c >= b:
	print(f"the biggest between {a}, {b}, {c} is {c}")

