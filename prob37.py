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

def satisfies(n):
    numstr = str(n)
    if len(numstr) < 2:
        return False
    for x in range(1, len(numstr)):
        if int(numstr[x:]) in prime_list and int(numstr[:x]) in prime_list:
            pass
        else:
            return False
    return True

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = 0
    total=0
    count = 0
    extend_prime_list(100000)
    i=0
    
    while count != 11:
        if satisfies(prime_list[i]):
            print prime_list[i]
            count+=1
            total+=prime_list[i]
        i+=1
        if i >= len(prime_list):
            extend_prime_list(prime_list[-1]+100000)
    
    time_end = time()
    print "Answer:", total
    print "Time taken", time_end-time_start
