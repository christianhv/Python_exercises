#!/usr/bin/env python

sentinel = '#quit'  # ends when this string is seen
line2 = ''
print "We will write a document. Type '#quit' to stop "
for line in '\n'.join(iter(raw_input, sentinel)):
    pass  # do things here
    line2 = line2 + line

print "%s" % line2


# To get every line as a string you can do:
#'\n'.join(iter(raw_input, sentinel))