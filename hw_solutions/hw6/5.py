def check_presence(integer, List):
	if len(List) == 0:
		return False
	if len(List) == 1:
		return integer == List[0]



print(check_presence(1, [0, 2, 3, 1, 2]))