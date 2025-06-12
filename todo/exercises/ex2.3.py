days = int(input('how many days?'))

if days < 1:
	print(0.0)
elif days == 1:
	print(50.00)
elif days == 2:
	print(90.00)
elif days == 3:
	print(120.00)
elif days == 4:
	print(140.00)
else:
	print(30*(days - 4) + 140)

