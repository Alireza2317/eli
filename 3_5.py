def sub_tuples(tup):
	for i in range(len(tup)+1):
		print(tuple(tup[:i]))



tup = (1, 13, 'ciao', True)
sub_tuples(tup)