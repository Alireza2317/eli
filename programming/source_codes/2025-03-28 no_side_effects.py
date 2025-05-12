# NO side effects

def printName(pn, fn, order):
    if order :
        return pn + " "+ fn
    else:
        return fn + " " + pn
        
personal = input("your name is: ")
family = input("your family name is: ")
printName(personal, family, True)
printName(personal, family, False)

#x = printName(personal, family, False)
print(printName(personal, family, False))