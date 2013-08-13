import sys
from time import time
from math import sqrt, floor, ceil

def decimal_digits(divisor):
    dividend_list=[]
    dividend = 10
    digits = []
    while dividend!=0 and not dividend in dividend_list:
        dividend_list.append(dividend)
        if dividend < divisor:
            dividend *= 10
        else:
            digits.append(dividend/divisor)
            dividend = (dividend % divisor)*10
        #print "dividend", dividend
    #print "digits", digits
    #print "dividend_list", dividend_list
    if dividend==0:
        return 0
    else:
        return len(dividend_list)-dividend_list.index(dividend)

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = 0
    total=0
    i=0
    
    for x in xrange(2, 1000):
        temp=decimal_digits(x)
        if temp > total:
            total=temp
            i=x
    time_end = time()
    print "Answer:", i
    print "Time taken", time_end-time_start
