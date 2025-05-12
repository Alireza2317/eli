#first program on functions

def maxVal(firstParam, secondParam):
    if firstParam > secondParam:
        return firstParam
    else:
        return secondParam
    
print(f"biggest between 3 and 5 is {maxVal(3,5)}")

print(f"biggest between 3+2 and 7 is {maxVal(3+2,7)}")

print(maxVal(1,2) * maxVal(3,2))

x = int(input("insert an integer number: "))
y = int(input("insert another integer number: "))

biggest = maxVal(x,y)

print(f"biggest of the two is {biggest}")
