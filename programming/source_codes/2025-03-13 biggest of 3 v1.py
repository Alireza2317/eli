#how to nest if statements
#biggest of 3 integers

print("give me 3 integers and I will choose the biggest of them")
a = int(input("give me the first integer "))
b = int(input("give me the second integer "))
c = int(input("give me the third integer "))

if a > b:
    #a is bigger than b, compare with c
    if a > c:
        print(f"the biggest is {a}")
    else:
        #a smaller than c
        print(f"the biggest is {c}")
else:
    #b is bigger than a, compare with c
    if b > c:
        print(f"the biggest is {b}")
    else:
        print(f"the biggest is {c}")
