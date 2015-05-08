#!/usr/bin/env python

# Create a mapping of state to abbreviation

states = {'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Michigan': 'MI'}

# Create a basic set of states and some cities in them
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville', 'NY': 'New York', 'OR': 'Portland'}


# Add some more cities


# print out some cities
print '-' * 10
print "NY State has: %s " % cities['NY']˜
print "OR state has: %s" % cities['OR']

# Print some states
print "-" * 10
print "Michigan abbreviation is: %s" % states['Michigan']
print "Florida abbreviation is: ", states['Florida']

# Do it by using the states and then the cities dict
print '-' * 10
print "Michigan has: %s" % cities[states["Michigan"]]
print "Florida has: %s" % cities[states["Florida"]]


# Print every state abbreviation
print "-" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# Print every city in state
print "-" * 10
for state, abbrev in states.items():
    print "%s has the city %s" % (state, cities[abbrev])

# Now do both at the same time
print "-" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has the city: %s" % (state, abbrev, cities[abbrev])

# Safely get an abbreviation by state that might not be there
print "-" * 10
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas"

# Get a city with a default value
city = cities.get('Texas', 'Does not exist')
print "The city for the state 'TX' is: %s" % city