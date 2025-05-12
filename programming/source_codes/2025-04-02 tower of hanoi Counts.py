#ex4_24.py
#tower of hanoi

#tower of hanoi: disks: number of disks, starting pole ending pole, temporary pole
def h(disks, starting, ending, temp):
    global numberOfCalls
    numberOfCalls += 1
    if disks == 1:                         #basic case
        return starting + "->" + ending + "\n"
    else:
     #recursive case
        return h(disks - 1, starting, temp, ending) + starting + "->" + ending + "\n"+ h(disks - 1, temp, ending, starting)

n = int(input("how many disks? "))
numberOfCalls = 0
print(h(n, "1", "3", "2"))
print(numberOfCalls)
