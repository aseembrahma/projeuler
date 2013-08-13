import sys
from time import time

prime_list = []

def build_primes(n):
    global prime_list
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

def exists_in_prime_list(n):
    for i in range(len(prime_list)-1, -1, -1):
        if n == prime_list[i]:
            return True
        elif n > prime_list[i]:
            return False
    return False

if __name__ == "__main__":
    time_start = time()
    limit = 1000000
    limit_lower = 0
    total=0
    count = 1
    
    build_primes(limit)
    prime_list_sum = sum(prime_list)
    prime_list_length = len(prime_list)
    full_prime_list_length = prime_list_length
    
    prime_list_last_valid_index = full_prime_list_length
    while prime_list_sum > prime_list[-1]:
        prime_list_sum -= prime_list[prime_list_last_valid_index-1]
        prime_list_length -= 1
        prime_list_last_valid_index -= 1
    
    max_sum = 0
    max_sum_length = 0
    
    for i in range(full_prime_list_length):
        current_sum = prime_list_sum
        current_length = prime_list_length
        if max_sum_length > (prime_list_length-i):
            break
        """
        j = full_prime_list_length
        
        while current_sum > limit:
            current_sum -= prime_list[j-1]
            current_length -= 1
            j -= 1
        """
        
        j = prime_list_last_valid_index
        
        #while current_sum not in prime_list:
        while not exists_in_prime_list(current_sum):
            current_sum -= prime_list[j-1]
            current_length -= 1
            j -= 1
        
        if current_length > max_sum_length:
            max_sum_length = current_length
            max_sum = current_sum
        #print current_sum, current_length
        prime_list_sum -= prime_list[i]
        prime_list_length -= 1
    
    time_end = time()
    print "Answer:", max_sum, max_sum_length
    print "Time taken", time_end-time_start
