#find a positive integer divisible by both 11 and 12
x = 1
while True:
    if x % 11 == 0 and x % 12 == 0:
        break
    x += 1
print(f"{x} is divisible by both 11 and 12")