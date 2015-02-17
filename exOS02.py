#!/usr/bin/env python
import subprocess
import sys
import os

#proc = subprocess.Popen(['tail', '-500', 'mylogfile.log'], stdout=subprocess.PIPE)
subprocess.Popen('echo $PWD', shell=True)
subprocess.Popen('echo $SHELL', shell=True)
current_Process = subprocess.Popen(['echo', '$0' ], shell=False, stdout=subprocess.PIPE)
for line in current_Process.stdout.readlines():
   print line.rstrip()
#proc = subprocess.Popen(['echo', $SHELL ], stdout=subprocess.PIPE)

'''
for line in proc.stdout.readlines():
print line.rstrip()
''' 
""""
You can also use triple-double quote
in order to have multiline comments and 
it looks better than with just the quote sign
"""

#print sys.path

print os.popen("echo $0").read()
current_Shell = subprocess.call("echo $0", shell=True)

print current_Shell

print subprocess.Popen("echo $0", stdout=subprocess.PIPE, shell=True).stdout.read()

print subprocess.Popen("echo $0", stdout=subprocess.PIPE, shell=True, executable="/bin/bash").stdout.read()


print subprocess.Popen("cat <(echo TEST)", stdout=subprocess.PIPE, shell=True, executable="/bin/bash").stdout.read()

#print subprocess.Popen("cat <(echo TEST)", stdout=subprocess.PIPE, shell=True).stdout.read()

from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    print "We are on Linux"
    _ls = "ls -la"
elif _platform == "darwin":
    print "We are on Mac"
    _ls = "ls -la"
elif _platform == "win32":
    print "We are on Windows"
    _ls = "dir"

output = subprocess.Popen(_ls, stdout=subprocess.PIPE, shell=True).stdout.read()
print output
