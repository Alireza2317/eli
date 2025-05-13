#def concatenate_indexwise(list1, list2):
#	output = []
#	for item1, item2 in zip(list1, list2):
#		output.append(item1+item2)

#	return output

def concatenate_indexwise(list1, list2):
	output = []

	for i in range(len(list1)):
		output.append(list1[i]+list2[i])

	return output


list1 = ["M", "na", "i", "An"]
list2 = ["y", "me", "s", "gelo"]

list3 = concatenate_indexwise(list1, list2)

print(list3)