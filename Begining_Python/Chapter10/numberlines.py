#!/usr/bin/python
# -*- coding: UTF-8 -*-

import fileinput
import shelve

#for line in fileinput.input(inplace=True):
for line in fileinput.input():
    line = line.rstrip()
    num  = fileinput.lineno()
    print ('%-40s # %2i' % (line, num))

s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
