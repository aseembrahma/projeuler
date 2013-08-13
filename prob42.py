import sys
from time import time

def word_value(s):
    total=0
    for x in s:
        total+=(ord(x)-ord('A')+1)
    return total

def triangle(n):
    return (n*(n+1))/2

if __name__ == "__main__":
    time_start = time()
    limit = 1000000
    limit_lower = 1
    total=0
    
    contents = [word_value(x.strip('"')) for x in open('words.txt').read().split(",")]
    #contents.sort(key=len)
    #values = [word_value(s) for s in contents]
    tempmax=max(contents)
    i = 0
    temp=0
    while i==0 or temp<tempmax:
        i+=1
        temp=triangle(i)
        if temp in contents:
            total+=contents.count(temp)
    print "Answer:", total
    time_end = time()
    print "Time taken", time_end-time_start
