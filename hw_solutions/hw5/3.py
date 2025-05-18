def map_lists(l1, l2):
	output = {}

	for i in range(len(l1)):
		#output.setdefault(l1[i], l2[i])
		output[l1[i]] = l2[i]

	return output

l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']

print(map_lists(l1, l2))