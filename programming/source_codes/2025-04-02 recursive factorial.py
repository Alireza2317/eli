#facorials

#iterative
def facI(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

#recursive
def facR(n):
    print(f"racursive factorial of {n}")
    if n == 1:
        return 1
    else:
        return n * facR(n-1)
    
#Bugged: tautology    
#def facB(n):
#    return facB(n)

n = int(input("insert the number: "))

print(f"iterative {facI(n)}")
print(f"recursive {facR(n)}")
#print(f"bugged {facB(n)}")
