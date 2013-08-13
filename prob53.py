import sys
from time import time
from math import sqrt

if __name__ == "__main__":
    time_start = time()
    limit = 100
    limit_lower = 0
    total=0
    count = 0
    
    factorial_list = [1]
    for n in xrange(1, limit+1):
        factorial_list.append(n*factorial_list[-1])
        for r in xrange(1, n):
            temp = factorial_list[n]/(factorial_list[r]*factorial_list[n-r])
            #print n, "C", r, "=", temp
            if  temp > 1000000:
                total+=1
    time_end = time()
    print "Answer:", total
    print "Time taken", time_end-time_start
