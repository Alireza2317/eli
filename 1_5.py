A = 'It is impossible'
#1
words = A.split()

max_length = 0
longest_word = ''

for word in words:
	if len(word) > max_length:
		max_length = len(word)
		longest_word = word

print(longest_word)









#2
#words = A.split()

#longest = max(words, key=len)

#print(longest)