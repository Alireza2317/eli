#biggest of 2 integers

print("give me 2 integers and I will choose the biggest of them")
a = int(input("give me the first integer "))
b = int(input("give me the second integer "))

if a > b:
    print(f"the biggest is {a}")
elif a < b:
    print(f"the biggest is {b}")
else:
    print("they are equal")