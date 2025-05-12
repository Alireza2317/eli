print('0: end program')
print('1: swap the (2*i)th and (2*i+1)th elements of S')
print('2: form all possible strings by shifting S one position to the left.')
print('3: reverses each word in S')

while True:
	op = input('Enter operation: ')
	if op == '0':
		print('end!')
		exit()
	else:
		S = input('Enter a string(S): ')
		if op == '1':
			i = 0
			result = ''
			while i < len(S)-1:
				result += S[i+1] + S[i]
				i += 2

			if len(S)%2 == 1:
				result += S[-1]

			print(result)

		elif op == '2':
			possible_strings = []
			for i in range(len(S)):
				possible_strings.append(S[i:] + S[:i])
			print(possible_strings)

		elif op == '3':
			words = S.split()
			result = ''
			for word in words:
				#result += reversed(word)
				result += word[::-1] + ' '

			print(result)
