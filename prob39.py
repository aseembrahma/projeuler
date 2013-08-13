import sys
from time import time
from math import sqrt

def satisfies(sidelist, n):
    sidelist.sort()
    if sum(sidelist)==n and (sidelist[0]**2)+(sidelist[1]**2)==(sidelist[2]**2):
        return True
    return False

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = 0
    total=0
    count = 0
    i=0
    
    triples = []
    perimeter_dict = {}
    for i in xrange(1, limit/2):
        for j in xrange(i, limit/2):
            temp=sqrt(i**2+j**2)
            if int(temp)==temp and temp < limit/2:
                triples.append([i, j, int(temp)])
                tempsum = i+j+int(temp)
                if tempsum in perimeter_dict:
                    perimeter_dict[tempsum] += 1
                else:
                    perimeter_dict[tempsum] = 1
    count = max(perimeter_dict.values())
    for x in perimeter_dict:
        if perimeter_dict[x]==count:
            print "Ans:", x
    time_end = time()
    print "Answer:", total
    print "Time taken", time_end-time_start
