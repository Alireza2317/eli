a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))
operator = input('Enter an operation: ')


#if operator == 'sum' or operator == '+'
if operator in ['sum', '+']:
	result = a + b
elif operator in ['sub', '-']:
	result = a - b
elif operator in ['mult', '*']:
	result = a * b
elif operator in ['div', '/']:
	result = a / b

print(result)