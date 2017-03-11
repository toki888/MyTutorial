#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import datetime

class FooBar:
    def __init__ (self, nikename='wenyun', birthday='1968/12/14'):
        self.nikename=nikename
        self.birthday=birthday

class A:
    def hello (self):
        print ( 'Hello, my name is wenyun' )

class B(A):
    def hello (self, greeting='Hello, my name is toki'):
        print ( greeting )

class CounterList(list):
   def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0
   def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self

def conflict (state, nextX):
    nextY = len(state)
    for i in range(nextY) :
        if abs(state[i]-nextX) in (0, nextY-1):
            return True
    return False

def queens (num=8, state=()):
    if len(state)==num-1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos





##################################################

#myObj = FooBar()
#myObj1 = FooBar('toki', '2000/1/4')

#print ( myObj.birthday )
#print ( myObj1.birthday )

#a=A()
#b=B()
#a.hello()
#b.hello()
#b.hello('Hello, world')

######
#cl=CounterList(range(10))
#print ( cl )
#cl.reverse()
#print ( cl )
#del cl[3:6]
#print ( cl, cl.counter)
#x=cl[4]+cl[2]
#print ( cl.counter )
#print ( cl,x )

fibs = Fibs()

fibs.next

for f in fibs:
    if f>1000:
        print ( f )
        break

print ( sys.argv )










