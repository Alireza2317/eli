#converting a score into a grade
#uses cascade if

score = int(input("insert the score: "))

if score >= 28 :
    print("the converison is A")
elif score >= 25:
    print("the converison is B")
elif score >= 22:
    print("the converison is C")
elif score >= 18:
    print("the converison is D")
else:
    print("the converison is F")