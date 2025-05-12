#greatest commond divisor

x = int(input("insert first number"))
y = int(input("insert second number"))

if x>y:
    gcd = y

else:
    gcd = x
    
while x%gcd!=0 or y%gcd!=0:
    gcd-=1
print(gcd)
