#read, print, and store a sequence of numbers using while loop
#find the maximum

l = []
element = input(f"insert the element ['enter' to stop]: ")

while element != "":
    l.append(int(element))
    element = input(f"insert the element ['enter' to stop]: ")

print(l)

maximum = l[0]
minimum = l[0]
total = 0

for i in l:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i
    total += i
average = total/len(l)

print(f"the biggest value is {maximum}, the minimum is {minimum} the average is {average}")