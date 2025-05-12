#solving the neighborhood problem
nc = int(input("insert the number of cities: "))

positions = []

for i in range(nc):
    positions.append(int(input(f"position of city {i+1}-th: ")))
positions.sort()

smallest_neighborhood = 1000000000000.0 # bigger than specificaitons

for i in range(1, nc-1):
    left = (positions[i] - positions[i-1])/2
    right = (positions[i+1] - positions[i])/2
    size = left + right
    if size < smallest_neighborhood:
        smallest_neighborhood = size
print(f"the smallest neighborhood is {smallest_neighborhood}")