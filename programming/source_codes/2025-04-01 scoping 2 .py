#another problematic (?) example of function
#generic name of a mathematical function
def f(x):
    def g():
        x = 'abc'
        print(f"inside g: x = {x}")
    def h():
        z = x
        print(f"inside h: z = {z}")
    x += 1
    print(f"inside f: x = {x}")
    h()
    g()
    print(f"inside f: x = {x}")
    return h
    
x = 3
z = f(x)
print(f"main: x = {x}")
print(f"main: z = {z}")
z()
