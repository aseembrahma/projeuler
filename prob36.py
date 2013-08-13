import sys
from time import time

if __name__ == "__main__":
    time_start = time()
    total = 0
    limit = 1000000
    limit_lower = 1
    
    # this can probably be combined with the above nested loop
    for i in range(limit_lower, limit+1):
        temp = str(i)
        if temp==temp[::-1]:
            temp=bin(i)[2:]
            if temp==temp[::-1]:
                total+=i
    print "Answer:", total
    time_end = time()
    print "Time taken", time_end-time_start
