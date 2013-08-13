import sys
from time import time
from math import sqrt, floor, ceil

def triangle(n):
    return (n*(n+1))/2

def pentagonal(n):
    return (n*((3*n)-1))/2

def hexagonal(n):
    return n*((2*n)-1)

def xgiveny(y):
    temp = sqrt(1-(4*(y-(3*(y*y)))))
    return (-1+temp)/2

def zgiveny(y):
    temp = sqrt(1-(4*y)+(12*y*y))
    return (1+temp)/4

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = 0
    total=0
    count=3
    y=0
    x=0
    z=0
    
    while count>0:
        y+=1
        temp = sqrt(1-(4*(y-(3*(y*y)))))
        if temp==int(temp):
            x=(-1+temp)/2
            if not x==int(x):
                continue
        else:
            continue
        temp = sqrt(1-(4*y)+(12*y*y))
        if temp==int(temp):
            z=(1+temp)/4
            if not z==int(z):
                continue
            else:
                if triangle(x)==pentagonal(y) and pentagonal(y)==hexagonal(z):
                    print x, y, z
                    count-=1
                    total=triangle(x)
                else:
                    continue
        else:
            continue
    time_end = time()
    print "Answer:", total
    print "Time taken", time_end-time_start
