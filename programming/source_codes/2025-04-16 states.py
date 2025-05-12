#ex7.15.py

states = {
        'Oregon':'OR',
        "Florida": "FL",
        "California":"CA",
        "New York": "NY",
        "Michigan": "MI"
        }
        
cities = {
        'CA': "San Francisco",
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }

#add some cities
cities['NY'] = 'New York'
cities["OR"] = "Portland"

print('_' * 20)
print(f"NY state has: {cities['NY']}")
print(f"OR state has: {cities['OR']}")

print('_' * 20)
print("Michigan's abbreviation os :", states['Michigan'])
print("Florida's abbreviation os :", states['Florida'])

print('_' * 20)
print(f"the state of Florida has: {cities[states['Florida']]}")
print(f"the state of California has: {cities[states['California']]}")

print('_' * 20)
#print(list(states.items()))
#print the states name and abbreviation
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")
    
#print every city in any state
print('_' * 20)
for abbrev, city in list(cities.items()):
    print(f"state {abbrev} has {city}")
    
#print complete name of states from the previous prints
print('_' * 20)
for state, abbrev in list(states.items()):
    print(f"{state} has city {cities[abbrev]}")


