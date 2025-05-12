tup = (1, 'hello', False, ' ', 'world', 2.5, '!')

def cat_strings(t):
	result = ''
	for item in t:
		if isinstance(item, str):
			result += item
	return result

print(cat_strings(tup))