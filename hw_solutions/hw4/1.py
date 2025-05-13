def get_level(tup_of_tups):
	tups = str(tup_of_tups)

	level = 0
	n_ignore = 0
	for char in tups:
		if char not in '()': continue

		if char == '(':
			if n_ignore == 0:
				level += 1
			else:
				n_ignore -= 1

		elif char == ')':
			n_ignore += 1

	return level



def flatten(tup_of_tups):
	n_level = get_level(tup_of_tups)
	for level in range(n_level):




test_tuple = ((1, (2, (1, 2))), (((1, 2), (1, 2)), (((1, 2), 2), (0 ,0))))


print(get_level(test_tuple))