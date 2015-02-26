#!/usr/bin/env python

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_no_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passangers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers."
print "There will be", cars_no_driven, "cars not driven"
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passangers_per_car, "persons in each car."
