# Exercise 39: Dictionaies, Oh Lovely Dictionaries

# create a mapping of state to abbreviation
states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' :  'NY',
	'Michigan' : 'MI',
}

# create a basic set of states and some cities in them
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreveation is: ", states['Florida']

# do it by using the state then the cities dictionary
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, No Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city of the state if 'TX' is: %s" % city

if states.has_key('New York'):
	print "states has_key 'New York'"
if not states.has_key('Texas'):
	print "states ! has_key 'Texas'"

print cities.keys()
print cities.values()
print states.items()

# Can operate on a dict if it contains strings
print ' '.join(cities)
cities_list = ['FL', 'CA', 'MI', 'OR', 'NY']
print ' '.join(cities_list)

# Cannot operate on a dict as if it were a list
print cities_list
# FIXME following returns None
print cities_list.reverse()
