def flatten(nested_list):
	flat = []
	stack = nested_list

	while stack:
		current = stack.pop()

		if isinstance(current, list):
			stack.extend(current)
		else:
			flat.append(current)

	return flat[::-1]

nested_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

print(*flatten(nested_list))