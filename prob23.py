import sys
from time import time
from math import sqrt

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

def is_abundant(n):
    temp=int(sqrt(n))
    sum=0
    for i in range(1, temp+1):
        if n%i == 0:
            sum+=i
            if i!=1 and i*i!=n:
                sum+=n/i
    return sum>n

if __name__ == "__main__":
    time_start = time()
    total = 0
    limit = 28124
    limit_lower = 10
    
    abundant_list = [x for x in range(limit_lower, limit+1) if is_abundant(x)]
    print len(abundant_list)
    
    
    abundant_sum_numbers = set()
    for i in range(len(abundant_list)):
        for j in range(i, len(abundant_list)):
            temp=abundant_list[i]+abundant_list[j]
            abundant_sum_numbers.add(abundant_list[i]+abundant_list[j])
            
    total=sum(set(range(1,limit)).difference(abundant_sum_numbers))
    print "Answer:", total
    time_end = time()
    print "Time taken", time_end-time_start
