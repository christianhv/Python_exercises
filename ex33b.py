#!/usr/bin/env python

i = 0
numbers = []


def mientras(it):
    if it < 6:
        print "At the top i is %d" % it
        numbers.append(it)

        it += 1

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % it
        mientras(it)


mientras(i)

print "The numbers: "

for num in numbers:
    print numbers
