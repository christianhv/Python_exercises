#!/usr/bin/env python

#This one is like the scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1 = %r, arg2 = %r" % (arg1,arg2)
    
#Ok, that *args is actually pointless, we can do just this
def print_two_again(arg1, arg2):
    print "arg1 = %r, arg2 = %r" % (arg1,arg2)
    
#This just print one argument
def print_one(arg1):
    print "arg1 = %r" % arg1
    
#this one takes no arguments
def print_none():
    print "I got nothing"
    
    
def main():
    print_two(5,"hola")
    print_two_again("bien", "eh")
    print_one("Pos nomas uno")
    print_none()
    

main()
    
    