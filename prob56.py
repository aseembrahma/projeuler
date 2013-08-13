import sys
from time import time

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = 0
    total=0
    count = 0
    
    for a in range(1, 100):
        for b in range(1, 100):
            temp = list(str(pow(a, b)))
            total=max(total, sum([int(x) for x in temp]))
    
    time_end = time()
    print "Answer:", total
    print "Time taken", time_end-time_start
