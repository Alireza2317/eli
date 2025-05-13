def del_dup(L: list):
	seen_items = set()
	to_remove_vals = []

	for item in L:
		if item in seen_items:
			to_remove_vals.append(item)
		else:
			seen_items.add(item)

	for val in to_remove_vals:
		for _ in range(L.count(val) - 1):
			L.remove(val)

L = [1, 3, 1, 5, 3, 3, 3, 4]

del_dup(L)

print(L)