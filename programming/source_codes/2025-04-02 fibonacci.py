#fibonacci 

#Assumes n int >= 0; Returns Fibonacci of n
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#prints the fibonacci series 
def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))


s = int(input("fibonacci for what number? : "))

print(f"fibonacci of {s} is {fib(s)}")
print("the corresponding sequence is")
print(testFib(s))

