



























def f(t):
	if not isinstance(t, tuple):
		return None

	i = 0
	while True:
		if not isinstance(t[i], int):
			return False

		i += 1

		if i == len(t):
			break

	i = 1
	while True:
		if t[i] <= sum(t[:i]):
			# not ok
			return False

		i += 1
		if i == len(t):
			return True
