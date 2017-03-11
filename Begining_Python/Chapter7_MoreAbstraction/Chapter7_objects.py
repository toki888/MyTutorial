#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

class Person:
    def setName(self, name):
         self.name = name

    def getName(self):
         return self.name

    def greet(self):
         print ("Hello, world! I'm %s." %self.name)

foo=Person()
bar=Person()
foo.setName('wenyun Shi')
bar.setName('abc')

y=foo.getName()
#print(y)
#print ( bar.getName())

#Person.greet(foo)

class Filter:
    def init (self):
        self.blocked = []
    def filter (self,sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):   #SPAMFilter is a subclass of Filter
    def init (self):        #Overrides ini method from Filter superclass
        self.blocked = ['SPAM', 'meal']

f=Filter()
f.init()
y=f.filter([1,2,3])
print ( y )

s=SPAMFilter()
s.init()
z=s.filter(['SPAM','SPAM','SPAM','ABC','SPAM','sPAM','bacon','egg','meal'])
print ( z )
print ( SPAMFilter.__bases__ )
#x=isinstance(f, Filter)
#print ( x )
print ( type(s) )

print ( 287*16.32 )

#for i in      time.strptime(time.asctime()) :

print ( time.strptime(time.asctime()) )


















