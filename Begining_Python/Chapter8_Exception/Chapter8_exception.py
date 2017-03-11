#!/usr/bin/python
# -*- coding: UTF-8 -*-

def mydiv (x,y):
    try:
        return x/y
    except (ZeroDivisionError) as e:
        print ( "The second number can't be zero!" )
        print ( e )

        return None

x=4;y=0
#print ( mydiv(x,y) )

try:
    4/10
except (ZeroDivisionError) as e:
    print ( e )

class foo:
    print ( 'Hello, World!' )


