#ex4_24.py
#tower of hanoi


#tower of hanoi: disks: number of disks, starting pole ending pole, temporary pole
def h(disks, starting, ending, temp, count):
    count += 1
    if disks == 1:                     #basic case
        return starting + "->" + ending + "\n"
    else:                              #recursive case
        return h(disks - 1, starting, temp, ending, count+1) + starting + "->" + ending + "\n"+ h(disks - 1, temp, ending, starting, count+2)


n = int(input("how many disks? "))
c = 0
print(h(n, "1", "3", "2",c))
print(c)
