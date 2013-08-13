"""
Problem 47
04 July 2003

The first two consecutive numbers to have two distinct prime factors are:

14 = 2  7
15 = 3  5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2**2  7  23
645 = 3  5  43
646 = 2  17  19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
"""

import sys
from copy import copy
from time import time, sleep
from math import sqrt, floor, ceil

prime_list = []


if __name__ == "__main__":
    time_start = time()
    limit = 100
    limit_lower = 0
    total = 0
    
    bit_list = [True for x in range(2, n+1)]
    for i in range(len(bit_list)):
        if bit_list[i]==False: continue
        x = i+2
        prime_list.append(x)
        temp = x+x
        while temp <= n:
            bit_list[temp-2]=False
            temp += x
    del bit_list
    
    time_end = time()
    print "Answer:", ''.join([str(x) for x in password])
    print "Time taken", time_end-time_start
