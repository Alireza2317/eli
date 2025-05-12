states = {
    'Oregon':'OR',
    'Florida': 'FL',
    'California' : 'CA',
    'New York' : 'NY' ,
    'Michigan' : 'MI'
}

cities = {
    'CA':'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
#add some cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' *10)
print(f"NY state has: {cities['NY']}")
print(f"OR state has: {cities['OR']}")

print('-' *10)
print(f"Michigan abbreviation is: {states['Michigan']}")
print(f"Florida abbreviation is: {states['Florida']}")

print('-' *10)
print(f"Michigan state has: {cities[states['Michigan']]}")
print(f"Florida state has: {cities[states['Florida']]}")

print('-' *10)
for state, abbreviation in list(states.items()):
    print(f"{state} has abbreviation {abbreviation}")

print('-' *10)
for abbreviation, city in list(cities.items()):
    print(f"{abbreviation} has city {city}")

print('-' *10)
for state, abbrev in list(states.items()):
    print(f"{state} has abbreviation {abbrev}")
    print(f"{abbrev} has city {cities[abbrev]}")

state = states.get('Texas')
print(state)

state = states.get('Texas','Sorry, we do not know Texas')
print(state)