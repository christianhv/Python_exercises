#!/usr/bin/env python


the_count = [1, 2, 3, 4, 5]

fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# the first kind of for-loop goes through a list
for number in the_count:
   print "This is count: %d " % number
   

#Same as above
for fruit in fruits:
   print "Fruit : %s" % fruit
   
#Also we can go through mixed lists too 
#notice we have to use %r sinde we don;t know what's in it
for i in change:
   print "This is change: %r" % i
   
#We can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
   print "Adding %d to the list" % i
   #append is a function that lists understand
   elements.append(i)
   
#Now we can print them out too.
for j in elements:
   print "This is an element: %d" % j