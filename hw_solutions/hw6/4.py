def flatten(nested_list):
	current = nested_list
	for item in current:
		if isinstance(current, list):
			flatten(item)
		else:
			print(item, end=' ')


nested_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

flatten(nested_list)
print()