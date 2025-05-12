#read, print, and store a sequence of numbers using for loop

n = int(input("insert the length of the sequence: "))
l = []

for i in range(n):
    element = int(input(f"insert the element n. {i+1}: "))
    l.append(element)
    
print(l)