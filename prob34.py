import sys
from time import time

def factorial(n):
    if n==0:
        return 1
    else:
        return reduce(lambda x, y: x*y, range(1,n+1))

if __name__ == "__main__":
    time_start = time()
    total = 0
    limit = 100000
    limit_lower = 3
    
    factorial_list = [factorial(x) for x in range(10)]
    for i in range(limit_lower, limit+1):
        if i==sum([factorial_list[int(x)] for x in str(i)]):
            total+=i
    print "Answer:", total
    time_end = time()
    print "Time taken", time_end-time_start
