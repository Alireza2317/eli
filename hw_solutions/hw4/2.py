def add_in_order(L, n):
	for i, element in enumerate(L):
		if n > element:
			if i == len(L) - 1:
				L.append(n)
				break

			continue

		if i < len(L):
			L.insert(i, n)
		break


L = [1,3,4,5,6]

n = 23

add_in_order(L, n)

print(L)