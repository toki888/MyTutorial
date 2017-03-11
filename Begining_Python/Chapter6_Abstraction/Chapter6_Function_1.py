#!/usr/bin/python
# -*- coding: UTF-8 -*-
def hello (name):
    return 'Hello,' + name + '!'

def square (x):
    'Calculates the square of the number x.'
    return x*x


#print ( hello('wenyun') )
#print ( square(19) )

def inc (x):
    x[0]=x[0]+1

foo=[10]
inc(foo)
print ( foo[0] )

def print_params (**params):
    print ( params )

#print_params(x=1, y=2, z=3)

def print_p (x, y, z=3, *p1, **p2):
    print ( '---------------------------' )
    print ( x, y, z )
    print ( p1 )
    print ( p2 )
    print ( locals()['p1'])


print_p (1,2, 4, 5,6,7,8,9,10,11)

def store (data, *full_names):
    for full_name in full_names:
        names=full_name.split()
        if len(names)==2: names.insert(1, '')
        labels = 'first','middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name]=[full_name]


def factorial (n):
    if n==1:
        return 1
    else:
        return n* factorial (n-1)

print ( factorial(5) )

def search(sequence, number, lower=0, upper=None):
     if upper is None: upper=len(sequence)-1

     if lower == upper:
          assert number == sequence[upper]
          return upper
     else:
          middle = (lower + upper) // 2
          if number > sequence[middle]:
                return search(sequence, number, middle+1, upper)
          else:
                return search(sequence, number, lower, middle)

seq = [34, 67, 8, 123, 4, 100, 95]
print(search (sorted(seq), 95))














