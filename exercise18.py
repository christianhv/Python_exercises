#!/usr/bin/env python

#This one is like the scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1 = %r, arg2 = %r" % (arg1,arg2)
    
#Ok, that *args is actually pointless, we can