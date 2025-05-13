# location_1 = left
#ball = left
# location_2 = middel
# locaation_3 = right
# A =1 ,2
# B = 2 ,3
# C = 1, 3

swaps = input(':')

Q =[1 , 2 , 3]


for swap in swaps.split():
	if swap == 'A':
		new_order =[Q[1] , Q[0] , Q[2]]
	if swap == 'B':
		new_order =[Q[0] , Q[2] , Q[1]]
	if swap == 'C':
		new_order =[Q[2] , Q[1] , Q[0]]

	Q = new_order


print (new_order.index(1)+1)

loc = new_order.index(1)
if loc == 0:
	print('left')
elif loc == 1:
	print('middle')
elif loc == 2:
	print('right')



