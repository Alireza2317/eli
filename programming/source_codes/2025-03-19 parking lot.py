# the problem of parking lot

today = input("insert the today occpuancy: ")
yesterday = input("insert the yesterday occpuancy: ")

popular = 0

for i in range(len(today)):
    if today[i] == "C" and yesterday[i] == "C":
        popular += 1

print(f"the number of 'popular' parking spaces is {popular}")