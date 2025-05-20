# > < == to check alphabetical order
# in
# not in
# string module
# strip
# f''

print(3 in [3, 4, 5])
print('oh' in 'hello there')
#the exact same match --> Ture; otherwise False
print('oh' not in 'hello there')


s = '     hello there    \n\n'

print(s)
print('----------')
print(s.strip())
print('----------')


s = '!!!hello! there!'

print(s.strip('!')) # 'hello! there'


import string

print('------')
print(string.ascii_letters)
print('------')
print(string.ascii_lowercase)
print('------')
print(string.ascii_uppercase)
print('------')
print(string.digits)
print('------')
print(string.punctuation)
print('------')
print(string.printable)
print('------')
print(string.whitespace)
print('------')

a = 2
b = 4.567

#s = f'sum is = {a+b}'

x = a + b
s = 'sum is = ' + str(x)

print(s)
#sum is =6.567

