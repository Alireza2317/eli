def function(L, a, b):
	d = {}

	for item in L:
		if item in d:
			d[item] += 1
		else:
			d[item] = 1

	output = []
	for item, count in d.items():
		if a <= count <= b:
			output.append(item)

	return output

L = [3,6,2,3,4,6,1,2,3,2,1,5,6]
a = 2
b = 3

print(function(L, a, b))
