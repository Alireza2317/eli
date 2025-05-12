t1 = (1, 2, 3, 4)

def reverse_tuple(t):
	return t[::-1]

def reverse_tuple(t):
	rev_list = []
	for i in range(len(t)-1, -1, -1):
		rev_list.append(t[i])
	return tuple(rev_list)


print(reverse_tuple(t1))