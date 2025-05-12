#find a positive integer divisible by both 11 and 12
#does not use break
x = 1
while x % 11 != 0 or x % 12 != 0:
    x += 1
print(f"{x} is divisible by both 11 and 12")