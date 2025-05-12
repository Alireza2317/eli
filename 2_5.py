string = 'Hello, World!'


lowers = ''
uppers = ''
for character in string:
	if character.islower():
		lowers += character
	if character.isupper():
		uppers += character

#print(lowers + uppers)
print(f'{lowers}{uppers}')