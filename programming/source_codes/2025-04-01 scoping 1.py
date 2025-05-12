#a problematic (?) example of function

#generic name of a mathematical function
def f(x): #x is the formal parameter
    y = 1
    x += y
    print(f"in f(x) x = {x}")
    return x
    
x = 7
y = 3
z = f(x)
print(f"z = {z}")
print(f"x = {x}")
print(f"y = {y}")
