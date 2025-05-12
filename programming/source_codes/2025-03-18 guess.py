# guess a secret number

secret = 312

n = int(input("insert an integer between 0 and 1000: "))

while n != secret:
    if n > secret:
        print("your guess is too big")
    else:
        print("your guess is too small")
    n = int(input("insert an integer between 0 and 1000: "))

print("the secret was",secret)