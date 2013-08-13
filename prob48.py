import sys
from time import time

def series(n):
    sum = 0
    for i in range(1, n+1):
        sum += pow(i,i)
    return sum

if __name__ == "__main__":
    time_start = time()

    n=1000
    sum = 0
    for i in range(1, n+1):
        sum += pow(i,i)
    print "Answer:", sum
    time_end = time()
    print "Time taken", time_end-time_start
