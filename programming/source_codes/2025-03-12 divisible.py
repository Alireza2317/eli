#check if a number is divisible by both 2 and 3

x = int(input("enter an integer number: "))

if x % 2 == 0:
    #x is divisible by 2
    if x % 3 == 0:
        print(f"{x} is divisible by both 2 and 3")
    else:
        print(f"{x} is divisible by 2 but not by 3")
elif x % 3 == 0: 
    print(f"{x} is divisible by 3 but not by 2")
else:
    print(f"{x} is not divisible by 2 neither by 3")
    
