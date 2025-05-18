def max_dict(d1, d2):
	for key, val in d2.items():
		if key not in d1:
			d1[key] = val
		else:
			d1[key] = max(d1[key], val)


d1 = {'a': 5, 'b': 9, 'c': 20}
d2 = {'a': 4, 'b': 11, 'd': 7}

max_dict(d1, d2)
print(d1)
