#usage of argv

from sys import argv

greens = argv[1]
yellows = argv[2]
blacks = argv[3]

optional = argv[4:]


print(f"greens {greens}")
print(f"yellows {yellows}")
print(f"blacks {blacks}")
print(f"optional {optional}")
    