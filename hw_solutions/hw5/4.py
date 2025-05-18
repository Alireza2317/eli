def max_dict(d1, d2):
	d = {}

	#for key in d1.keys():
	#for key in d1:

	for key, val in d1.items():
		if key not in d:
			d[key] = val

	for key, val in d2.items():
		if key not in d:
			d[key] = val
		else:
			d[key] = max(d[key], val)

	return d

d1 = {'a': 5, 'b': 9, 'c': 20}
d2 = {'a': 4, 'b': 11, 'd': 7}

d = max_dict(d1, d2)
print(d)
