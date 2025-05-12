# power of an integer the hard way
# only positive integers allowed

base = int(input("please insert the base number: "))
exponent = int(input("please insert the exponent number: "))

result = 1

while exponent >= 1:
    result *= base
    exponent -= 1
    
print(f"the result is {result}")