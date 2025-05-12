# guess a secret number, the secret is form the user

guess = 500
step = 500

answer = input(f"what about {guess} (s=smaller; b=bigger; ok=ok): ")

while answer != "ok":
    step = step // 2
    if step == 0:
        step = 1
    if answer == "b":
        guess -= step
    elif answer == "s" :
        guess += step
    else:
        print("I do not understand your answer, please repeat")
    answer = input(f"what about {guess} (s=smaller; b=bigger; o=ok): ")
print("I won!!!! the secret is",guess)