A = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
B = 's'

##1
#first = -1
#for index, character in enumerate(A):
#	if character == B:
#		if first < 0:
#			first = index
#		last = index

#print(first, last)
#print(A[first:last+1])


#2
first_occur_index = A.index(B)
last_occur_index = A.rindex(B)

print(A[first_occur_index:last_occur_index+1])



#3
first_occur_index = A.index(B)

last_occur_index = len(A) - A[::-1].index(B) - 1

print(A[first_occur_index:last_occur_index+1])


#3
#first_occur_index = A.index(B)

#last_occur_index = -A[::-1].index(B) -1

#print(A[first_occur_index:last_occur_index+1])
