#ex4_19.py
#fibonacci and counts calls to the function

ncals = 0 #this has to be globally referenced

#Assumes n int >= 0; Returns Fibonacci of n
def fib(n):
    global ncals  # referencing the global variable ncals
    ncals += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

		
s = int(input("fibonacci for what number? : "))

print(f"fibonacci of {s} is {fib(s)}")
print("to compute it the funciton was called", ncals, "times")

