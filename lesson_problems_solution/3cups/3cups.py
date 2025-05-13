swaps = input().split()

ball_loc = 1

for swap in swaps:
	if ball_loc == 1:
		if swap == 'A':
			ball_loc = 2
		elif swap == 'C':
			ball_loc = 3
	elif ball_loc == 2:
		if swap == 'A':
			ball_loc = 1
		elif swap == 'B':
			ball_loc = 3
	elif ball_loc == 3:
		if swap == 'B':
			ball_loc = 2
		elif swap == 'C':
			ball_loc = 1

#for swap in swaps:
#	if swap == 'A':
#		if ball_loc == 1:
#			ball_loc = 2
#		elif ball_loc == 2:
#			ball_loc = 1
#	elif swap == 'B':
#		if ball_loc == 2:
#			ball_loc = 3
#		elif ball_loc == 3:
#			ball_loc = 2
#	elif swap == 'C':
#		if ball_loc == 1:
#			ball_loc = 3
#		elif ball_loc == 3:
#			ball_loc = 1

print(ball_loc)