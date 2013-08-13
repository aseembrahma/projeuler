import sys
from time import time

def run_chain(n):
    x = n
    i = 1
    full_list = []
    
    while not x is 1:
        full_list.append(x)
        if x%2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        i = i + 1

    print full_list
    return i

def brute_force():
    max_length = -1
    for i in range(1,1000000):
        if i%10000==0: print i
        max_length=max(max_length, run_chain(i))
    print max_length

time_start = time()
length_dict = {}
length_dict[1] = 1
for i in range(1000000, 1, -1):
    x = i
    full_list = []
    while not x in length_dict:
        full_list.append(x)
        if x%2 == 0:
            x = x/2
        else:
            x = 3*x + 1
    while len(full_list):
        temp=full_list.pop()
        length_dict[temp] = 1+length_dict[x]
        x = temp
print length_dict.values().index(max(length_dict.values()))
time_end = time()
print time_end-time_start