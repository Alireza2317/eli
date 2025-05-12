#problem 3: basketball scores
print("enter the scores recorded for the Bananas team")
bananas3 = int(input("how many 3-point scores for the team "))
bananas2 = int(input("how many 2-point scores for the team "))
bananas1 = int(input("how many 1-point scores for the team "))

print("enter the scores recorded for the Apples team")
apples3 = int(input("how many 3-point scores for the team "))
apples2 = int(input("how many 2-point scores for the team "))
apples1 = int(input("how many 1-point scores for the team "))

bananasTotal = bananas3 * 3 + bananas3 * 2 + bananas1*1
applesTotal = apples3 * 3 + apples3 * 2 + apples1*1

if applesTotal > bananasTotal:
    print("Apples win!")
    print(applesTotal, " to", bananasTotal)
if applesTotal < bananasTotal:
    print("Bananas win!")
    print(bananasTotal, " to", applesTotal)
if applesTotal == bananasTotal:
    print("tie match between Bananas and Apples")
    print(bananasTotal, " even")
