import sys
from time import time
from math import sqrt
from collections import deque

def all_orderings(n):
    temp=deque(str(n))
    orderings = []
    for i in range(len(temp)):
        temp.rotate(-1)
        orderings.append(int(''.join(list(temp))))
    return orderings

if __name__ == "__main__":
    time_start = time()
    limit = 1000000
    limit_lower = 2
    total=0
    all_numbers = [True for x in range(limit_lower, limit)]
    for i in range(limit_lower, limit):
        if not all_numbers[i-limit_lower]:
            continue
        else:
            for j in range(i*limit_lower, limit, i):
                all_numbers[j-limit_lower] = False
    for i in range(limit_lower, limit):
        if all_numbers[i-limit_lower]:
            temp=all_orderings(i)
            tempsum=0
            for x in temp:
                if all_numbers[x-limit_lower]:
                    tempsum+=1
            if tempsum==len(temp):
                total+=1
    print "Answer:", total
    time_end = time()
    print "Time taken", time_end-time_start
