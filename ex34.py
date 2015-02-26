#!/usr/bin/env python

animals = ['bear', 'tiger', 'penguin', 'zebra']

for animal in animals:
   print animal
   
list_len = len(animals)
print "\n The lenght of the list is %d \n" % list_len

for i in range(0, list_len):
   print "The element %d in the list of animals is %s" % (i + 1, animals[i])