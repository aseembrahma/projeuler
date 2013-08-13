import sys
from time import time
from itertools import permutations

prime_list = []

def create_prime_list(n):
    global prime_list
    
    big_list = [True for x in range(2, n+1)]
    x = 2
    while x < n+1:
        #print "x", x
        if big_list[x-2]==True:
            i = x*2
            while i < n+1:
                #print "i", i
                big_list[i-2]=False
                i+=x
        x+=1
    for x in range(len(big_list)):
        if big_list[x]:
            prime_list.append(x+2)
    del big_list

def create_prime_list_less_memory(n):
    global prime_list
    
    for x in xrange(2, n+1):
        is_divisible = False
        for y in prime_list:
            if x%y == 0:
                is_divisible=True
                break
        if not is_divisible:
            prime_list.append(x)

def is_prime(n):
    print "Checking", n
    temp = list(str(n))  
    for x in xrange(2, n):
        if n % x == 0:
            return False
    return True

def satisfies(n):
    numlist = list(str(n))
    numlist.sort()
    return numlist==[str(x) for x in range(1, len(numlist)+1)]

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = 0
    total=0
    count = 0
    digits=9
    #since 1+2+3+4...+9 is div by 3, so is 1+2+...+8
    create_prime_list(7654321)
    for x in range(len(prime_list)-1, -1, -1):
        if satisfies(prime_list[x]):
            total = prime_list[x]
            break
    """
    while digits >=2:
        templist = range(1, digits+1)
        if sum(templist)%3 == 0:
            digits-=1
            continue
        for x in permutations(templist):
            print x
            if x[-1] in [2,4,6,8,0,5]:
                continue
            temp=int(''.join([str(y) for y in x]))
            if is_prime(temp):
                total = max(total, temp)
        digits-=1
        if total != 0:
            break
    """
    time_end = time()
    print "Answer:", total
    print "Time taken", time_end-time_start
