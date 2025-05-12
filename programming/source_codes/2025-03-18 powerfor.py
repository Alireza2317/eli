#power the hard way

base = int(input("insert the base: "))
exponent = int(input("insert the exponent: "))

res = 1

for mult in range(exponent):
    res = res * base
    
print(f" {base} elevated to {exponent} is {res}")


    