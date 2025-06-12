from random import randint

class Game:
	def __init__(self, nickname, initial_score, n_dices):
		self.name = nickname
		self.score = initial_score
		self.n = n_dices


	def bet(self, amount):
		if self.score < amount:
			print('Your score is too low!')
			return

		dices = [randint(1, 6) for _ in range(self.n)]
		print(f'Your dices: {dices}')

		# if all of them are 6, add bet to score
		comparisons = [(dices[i] == 6) for i in range(self.n)]
		if all(comparisons):
			self.score += amount
			print(f'You won the bet! Your score: {self.score}')
			return

		# if all of them are 1, subtract bet from score
		comparisons = [(dices[i] == 1) for i in range(self.n)]
		if all(comparisons):
			self.score -= amount
			print(f'You lost the bet! Your score: {self.score}')
			return

		# otherwise:
		print('Nothing happened!')


game = Game('eli', initial_score=15, n_dices=4)
game.bet(5)
