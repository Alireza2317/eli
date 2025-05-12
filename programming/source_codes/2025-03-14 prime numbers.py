#check if a integer number is prime
#no optimizations

n = int(input("insert the number to  chek :"))

divisor = 2

while n % divisor != 0:
    divisor += 1

if divisor == n:
    print("prime")
else:
    print("NOT prime")
    