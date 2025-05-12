#ex3_8.py
# showing approximation of numbers

x = 0.0

for i in range(10):
    x += 0.1

if x == 1.0:
    print(f"everthing Ok x = {x}")
else:
    print(f"Ho no: my computer failed; x = {x}")

xx = 0.1 * 10

print(xx)
print (xx == 1.0)