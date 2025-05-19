filename = 'testfile.txt'

def count_vowels(filename):
	d = {}

	with open(filename, 'r') as file:
		content = file.read()

	for character in content:
		if character in 'aeuioAEUIO':
			if character in d:
				d[character] += 1
			else:
				d[character] = 1

	return d

print(count_vowels(filename))