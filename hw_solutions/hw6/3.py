departure_city = input('Enter departure city: ')
arrival_city = input('Enter arrival city: ')
prefered_time = input('prefered time slot [e.g. 8:00-23:00]: ')





with open('flights.txt', 'r') as flight_file:
	flights = flight_file.read()

for line in flights.split('\n'):
	dep, dest, _, dep_time, arr_time = line.split()

	if dep == departure_city and dest == arrival_city and prefered_time == dep_time:
		with open('holidays_plan.txt', 'w') as file:
			file.write(line)
		print('found a flight!')

