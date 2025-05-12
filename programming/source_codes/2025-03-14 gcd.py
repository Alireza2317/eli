#find the greatest common divisor betwen two numbers.
#Higly bugged
x = int(input("insert the first number: "))
y = int(input("insert the second number: "))

#find the smallest and biggest
if x <= y:
    smallest = x
    biggest = y
else:
    smallest = y
    biggest = x


while biggest % smallest != 0:
    smallest -= 1

print(f"the biggest common divisor is {smallest}")