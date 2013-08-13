import sys
from time import time, sleep
from math import sqrt, floor, ceil

def sort_string(s):
    temp=[x for x in s]
    temp.sort()
    return ''.join(temp)

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = 0
    num_digits = 1
    max_factor = 6
    i = None
    
    while i is None:
        upper_limit = (pow(10, num_digits)-1)/max_factor
        lower_limit = pow(10, num_digits-1)
        for num in xrange(lower_limit, upper_limit+1):
            sorted_string=sort_string(str(num))
            for x in range(2, max_factor+1):
                #print num, x*num
                if sort_string(str(x*num)) != sorted_string:
                    break
                if x==max_factor:
                    i=num
            #sleep(2)
        num_digits+=1
    
    time_end = time()
    print "Answer:", i
    print "Time taken", time_end-time_start
