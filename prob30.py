import sys
from time import time

def digit_powered(num, power):
    total=0
    for x in str(num):
        total+=pow(int(x), power)
    return total

if __name__ == "__main__":
    time_start = time()
    total = 0
    limit = 1000000
    power = 5
    
    for i in range(2, limit+1):
        if digit_powered(i, power)==i:
            print i
            total+=i
    print "Answer:", total
    time_end = time()
    print "Time taken", time_end-time_start
