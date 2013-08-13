import sys
from time import time
from itertools import permutations

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = 0
    total=0
    count = 0
    product_set = set()
    
    for num in permutations(range(1, 10)):
        n=''.join([str(x) for x in num])
        #print n
        for x in range(1, 4+1):
            for y in range(1, (len(n)-x)/2 + 1):
                #print int(n[:x]), "*", int(n[x:x+y]), "=", int(n[x+y:])
                if int(n[:x])*int(n[x:x+y])==int(n[x+y:]):
                    product_set.add(int(n[x+y:]))
        """
        if count==5:
            break
        count+=1
        """
    time_end = time()
    print "Answer:", sum(product_set)
    print "Time taken", time_end-time_start
