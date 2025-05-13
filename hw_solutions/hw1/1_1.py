days = 'Sun Mon Tue Wed Thu Fri Sat'

days_list = days.split()
# ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

#1
for word in days_list:
	print('"' + word + '"')


#2
print(days.replace(' ', '\n'))

#3
print(*days.split(), sep='\n')

float
int
str
