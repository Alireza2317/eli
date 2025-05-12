#converting a score into a grade
#uses nested if

score = int(input("insert the score: "))

if score >= 28 :
    print("the converison is A")
else:
    if score >= 25:
        print("the converison is B")
    else:
        if score >= 22:
            print("the converison is C")
        else:
            if score >= 18:
                print("the converison is D")
            else:
                print("the converison is F")