import sys
from time import time
from math import sqrt

def satisfies(a, b):
    stra=str(a)
    strb=str(b)
    if stra[0] in strb:
        temp=strb.index(stra[0])
        if temp==0:
            if int(strb[1]) != 0 and float(a)/b == float(stra[1])/int(strb[1]):
                return True
        else:
            if int(strb[0]) != 0 and float(a)/b == float(stra[1])/int(strb[0]):
                return True
    elif stra[1] in strb and not int(stra[1])==0:
        temp=strb.index(stra[1])
        if temp==0:
            if int(strb[1]) != 0 and float(a)/b == float(stra[0])/int(strb[1]):
                return True
        else:
            if int(strb[0]) != 0 and float(a)/b == float(stra[0])/int(strb[0]):
                return True
    return False

if __name__ == "__main__":
    time_start = time()
    limit = 100
    limit_lower = 0
    total=0
    count = 0
    
    prod_num = 1
    prod_denom=1
    for i in xrange(10, limit):
        for j in xrange(i+1, limit):
            if satisfies(i, j):
                print i, "/", j
                prod_num *= i
                prod_denom *= j
    time_end = time()
    print "Answer:", prod_denom/prod_num
    print "Time taken", time_end-time_start
