#side effects

def printName(pn, fn, order):
    if order :
        print(pn, " ", fn)
    else:
        print(fn, " ", pn)
    return "done!"
        


personal = input("your name is: ")
family = input("your family name is: ")
printName(personal, family, True)
printName(personal, family, False)

x = printName(personal, family, False)

print(x)