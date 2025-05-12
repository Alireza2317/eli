#more on scoping

def f():
    print(f"inside f x={x}")
    
def g():
    x = 1
    print(f"inside g x={x}")
    
x = 3
f()
x = 10
g()
print(x)
