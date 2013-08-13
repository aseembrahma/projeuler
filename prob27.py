import sys
from time import time
from itertools import product
from copy import copy

prime_list = [2,3,5,7]

def extend_prime_list(n):
    global prime_list
    
    current_last_prime = prime_list[-1]
    if current_last_prime >= n:
        return
    numlist = [True for x in range(current_last_prime+1, n+1)]
    for i in prime_list:
        temp=((current_last_prime/i)+1)*i
        while temp<=n:
            numlist[temp-(current_last_prime+1)]=False
            temp+=i
    for i in range(len(numlist)):
        if numlist[i]:
            temp=i+(current_last_prime+1)
            prime_list.append(temp)
            temp+=(i+(current_last_prime+1))
            while temp<=n:
                numlist[temp-(current_last_prime+1)]=False
                temp+=(i+(current_last_prime+1))

def formula(n, a, b):
    return (n*n)+(n*a)+b

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = -1000
    #limit = 50
    #limit_lower = -50
    total=0
    max_a = None
    max_b = None
    max_n = 0
    extend_prime_list(1000)
    blist = copy(prime_list)
    extend_prime_list(100000)
    print "done"
    #n=0
    i=0
    
    for x in product(xrange(limit_lower+1, limit), blist):
        n=1
        while True:
            i+=1
            #temp = formula(n, x[0], x[1])
            temp = (n*n)+(n*x[0])+x[1]
            if temp<=0:
                break
            if temp > prime_list[-1]:
                extend_prime_list(temp)
                print "here"
            if temp in prime_list:
                n+=1
            else:
                break
        if n > max_n:
            max_n = n
            max_a = x[0]
            max_b = x[1]
    
    time_end = time()
    print "i =",i
    print "Answer:", max_a, max_b, max_n
    print "Time taken", time_end-time_start
