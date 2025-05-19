import string

filename = 'testfile.txt'

def count_words():
	with open(filename, 'r') as file:
		content = file.read()

	return len(content.split())


def count_visible():
	with open(filename, 'r') as file:
		content = file.read()

	count = 0
	for char in content:
		if char in string.ascii_letters+string.punctuation+string.digits:
			count += 1

	return count

def count_visibleAndSpace():
	with open(filename, 'r') as file:
		content = file.read()

	count = 0
	for char in content:
		if char in string.ascii_letters+string.punctuation+' ':
			count += 1

	return count

def count_characters():
	with open(filename, 'r') as file:
		content = file.read()

	return len(content)

def count_lines():
	with open(filename, 'r') as file:
		content = file.read()

	return len(content.split('\n'))

print(count_words())
print(count_visible())
print(count_visibleAndSpace())
print(count_characters())
print(count_lines())


