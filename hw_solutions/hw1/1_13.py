#import math
from math import sqrt

a = 7
b = -6
c = 9

delta = b*b - 4*a*c

if delta == 0:
	solution = -b / (2*a)
	print(f'x = {solution}')
elif delta < 0:
	print('No real solutions!')
else:
	solution1 = (-b + sqrt(delta)) / (2*a)
	solution2 = (-b - sqrt(delta)) / (2*a)

	print(f'x = {solution1}')
	print(f'x = {solution2}')