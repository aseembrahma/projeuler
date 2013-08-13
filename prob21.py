import sys
from time import time
from math import sqrt

def sum_divisors(n):
    temp=int(sqrt(n))
    sum=0
    for i in range(1, temp+1):
        if n%i == 0:
            sum+=i
            if i!=1 and i*i!=n:
                sum+=n/i
    return sum

if __name__ == "__main__":
    time_start = time()
    limit=10000
    all_nums=[]
    contents = [sum_divisors(x) for x in range(limit)]
    for i in range(len(contents)):
        x = contents[i]
        if x<limit and contents[x]==i and x!=i:
            all_nums.append(x)
            all_nums.append(contents[x])
    print "Answer:", sum(set(all_nums))
    time_end = time()
    print "Time taken", time_end-time_start
