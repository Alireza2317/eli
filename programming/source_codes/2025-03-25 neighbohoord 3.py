#solving the neighborhood problem
nc = int(input("insert the number of cities: "))

positions = []
sizes = []

for i in range(nc):
    positions.append(int(input(f"position of city {i+1}-th: ")))
positions.sort()
    
for i in range(1, nc-1):
    left = (positions[i] - positions[i-1])/2
    right = (positions[i+1] - positions[i])/2
    sizes.append(left + right)
    
print(f"the smallest neighborhood is {min(sizes)}")