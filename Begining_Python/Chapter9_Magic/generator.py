#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 

for f in fab(100):
    if f > 1000:
        print (f)
        break
    else:
        pass

    