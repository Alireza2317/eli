#ex4_19.py
#fibonacci and counts calls to the function


#Assumes n int >= 0; Returns Fibonacci of n
def fib(n):
    print(f"fib({n})")
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


s = int(input("fibonacci for what number? : "))

print(f"fibonacci of {s} is {fib(s)}")

