#read, print, and store a sequence of numbers using while loop
#find the maximum

l = []
element = input(f"insert the element ['enter' to stop]: ")

while element != "":
    l.append(int(element))
    element = input(f"insert the element ['enter' to stop]: ")    
    
print(l)

maximum = l[0]

for i in range(1,len(l)):
    if l[i] > maximum:
        maximum = l[i]
    
print(f"the biggest value is {maximum}")