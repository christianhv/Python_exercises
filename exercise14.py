#!/usr/bin/env python

from sys import argv

script, username = argv

prompt = "> "

print "Hi %s, I am the %s script." % (username, script)
print "I would like to ask you a few questions..."
print "Do you like me %s ?" % username
likes = raw_input(prompt) 

print "Where do you live %s?" % username
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a(n) %r computer. Nice.
""" % (likes, lives, computer)
