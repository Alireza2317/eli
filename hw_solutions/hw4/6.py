def draw_grid(grid):
	for i, row in enumerate(grid, 1):
		print(i, end=': ')
		print(*row, sep='\t')

	print()

def is_game_over(grid):
	# cheking rows
	for row in grid:
		if len(set(row)) == 1 and row[0] != '-':
			return True, row[0]

	#cheking columns
	for col in range(4):
		s = set()
		for row in grid:
			s.add(row[col])

		val = s.pop()

		if len(s) == 0 and val != '-':
			return True, val


	# check tie
	for row in grid:
		if '-' in row:
			# no tie, because grid is not full yet
			break
	else:
		# if no '-' found
		return True, '-'



	return False, None


def switch_turn(current_turn):
	new_turn = 'o' if current_turn=='x' else 'x'
	if current_turn == 'x':
		new_turn = 'o'
	else:
		current_turn = 'x'

	return new_turn

# empty grid
grid = [
	['-' for _ in range(4)]
	for _ in range(4)
]

turn = 'x'

draw_grid(grid)

while not is_game_over(grid)[0]:
	move = int(input(f'Insert move for "{turn}": '))

	if move > 4 or move < 1:
		print('invalid move!')
		continue


	# convert to python indices
	move -= 1


	# row is full
	if '-' not in grid[move]:
		print('chosen row is full!')
		continue


	# insert the move
	for i, cell in enumerate(grid[move]):
		if cell == '-':
			grid[move][i] = turn
			break


	draw_grid(grid)

	turn = switch_turn(turn)

result, winner = is_game_over(grid)


if winner in 'xo':
	print(f'{winner} won the game!')
else:
	print(f'tie!')
