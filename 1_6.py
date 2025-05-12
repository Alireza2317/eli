N = 5

#1
#num_circles = 1
#num_spaces = N - 1

#for line in range(N):
#	#print(num_spaces*' ' + num_circles*'o')
#	print(f'{num_spaces * " "}{num_circles * "o"}')
#	num_circles += 2
#	num_spaces -= 1

#print(f'{(N-1) * " "}o')


#2
#for line in range(1, N+1):
#	num_circles = line*2 - 1
#	print(f'{num_circles*"o":^{N*2-1}}')
#print(f'{"o":^{N*2-1}}')