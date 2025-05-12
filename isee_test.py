income = int(input('Enter income: '))
meter = float(input('Enter house area: '))

euro_price = float(input('Enter euro price (0 to use default): '))

if euro_price == 0:
	euro_price = 19_000

X = 2.85

income_euro = income * 1_000_000 / euro_price

house_value = 0.2 * 500 * meter

isee = (income_euro + house_value) / X

print(isee)

