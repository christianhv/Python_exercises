#!/usr/bin/env python

import os
def getShellName():
    val = os.popen("echo $0")
    return val.readlines()[0].strip()
    

valOS = getShellName()

print valOS