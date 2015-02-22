#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "christian"
__date__ = "$Feb 22, 2015 10:54:59 PM$"


ten_things = "Apples Oranges Crows Telephones Light Sugar"
print "Wait ther;s not 10 things in that list, let's fix that."
stuff = ten_things.split(' ') 
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff"

print stuff[1]
print stuff[-1] # Whoa! Fancy

print stuff.pop()

print ' '.join(stuff) # what? cool!

print '#'.join(stuff[3:5]) # Super stellar!




if __name__ == "__main__":
    print "Hello World"
