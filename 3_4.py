def check_minimum(tup_of_tups):
	minimum = min(tup_of_tups[0])

	for tup in tup_of_tups:
		if min(tup) != minimum:
			return False

	print(minimum)
	return True

tups = ((1, 13, 12), (5, 1), (6, 1, 3, 2))
print(check_minimum(tups))