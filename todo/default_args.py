# default arguments
# keyword arguments
# orders

def function(first, second):
	return first / second

# positional arguments
#print(function(5, 9))

# keyword(named) arguments
#print(function(second=24, first=48))

# SyntaxError
#print(function(first=50, 10))

# keyword args CAN follow positional args -> OK
#print(function(50, second=10))


# default argument
#def function(first, second=2):
#	return first / second

def function(first, second, printit=True):
	result = first / second

	if printit:
		print(result)

	#return result

print(function(18, 2))