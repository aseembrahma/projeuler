import sys
from time import time
from itertools import permutations, combinations

total=0

def concatenated_product(n):
    numstr = str(n) + str(2*n)
    if int(str(total)[:len(numstr)]) > int(numstr):
        return 0
    i = 3
    while len(numstr) < 9:
        if not satisfies_intermediate(i*n):
            return 0
        numstr += str(i*n)
        i+=1
    if len(numstr) != 9:
        return 0
    elif satisfies(numstr):
        return int(numstr)

def satisfies_intermediate(n):
    temp=[int(x) for x in list(str(n))]
    return len(temp)==len(set(temp))

def satisfies(n):
    temp=list(str(n))
    temp.sort()
    return temp==[str(x) for x in range(1, 10)]

if __name__ == "__main__":
    time_start = time()
    limit = 333333333+1
    limit_lower = 0
    total=0
    count = 1
    digits=4
    
    #for i in xrange(limit, 1, -1):
    while digits > 0:
        for i in combinations(range(1, 10), digits):
            for j in permutations(i):
                num=int(''.join([str(k) for k in j]))
                if len(str(2*num)) > 9 or not satisfies_intermediate(2*num):
                    continue
                total=max(total, concatenated_product(num))
        digits-=1
    time_end = time()
    print "Answer:", total
    print "Time taken", time_end-time_start
