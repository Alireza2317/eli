from mylib import *

def apply_to_each(l,f):
    for i in range(len(l)):
        l[i] = f(l[i])

l = []
intReadList(l)
print(l)

l1 = l
print(f"id(l) == id(l1) {id(l) , id(l1)}")

l2 = l[:]
print(f"id(l) == id(l2) {id(l) , id(l2)}")

apply_to_each(l,recursiveFactorial)
print(l)

print([recursiveFactorial(x) for x in l2]) #same as apply_to_each using list comprehension


