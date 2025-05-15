x = 12
y = -7

print((x > 0) or (y > 0))
print((x > 0) and (y > 0))

# and: returns the first if falsy  else the second
# or:  returns the first if truthy else the second


name = ''
print('hello ' + (name or 'user23'))

# falsy
falsies = [
	False, '', [], tuple(), list(), set(), 0, int(), float(), None, dict()
]

#truthy
#anything other than those above


# bool
for f in falsies:
	print(bool(f))