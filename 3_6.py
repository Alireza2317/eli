tups = (1, 2, (3.1, 3.2), 4, 5, (6.1, (6.2, 6.2), 6.3), 7)

def flatten(tups):
	result = []

	for item in tups:
		if isinstance(item, tuple):
			result.extend(flatten(item))
		else:
			result.append(item)
	return tuple(result)

print(flatten(tups))