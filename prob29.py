import sys
from time import time

if __name__ == "__main__":
    time_start = time()
    total = 0
    limit = 100
    limit_lower = 2
    distinct_terms = set()
    
    # this can probably be combined with the above nested loop
    for i in range(2, limit+1):
        for j in range(i, limit+1):
            distinct_terms.add(pow(i, j))
            distinct_terms.add(pow(j, i))
    print "Answer:", len(distinct_terms)
    time_end = time()
    print "Time taken", time_end-time_start
