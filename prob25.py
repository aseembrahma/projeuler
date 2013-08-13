import sys
from time import time

def fib(n):
    if n==1: return 1
    elif n==2: return 1
    else:
        first = 1
        second = 1
        for i in range(3, n+1):
            temp = second
            second = second+first
            first = temp
        return second

if __name__ == "__main__":
    time_start = time()

    first = 1
    second = 1
    i=2
    while len(str(second))!=1000:
        temp = second
        second = second+first
        first = temp
        i+=1
    print "Answer:", i
    time_end = time()
    print "Time taken", time_end-time_start
