import sys
from time import time

if __name__ == "__main__":
    time_start = time()
    limit = 7830457
    limit_lower = 0
    total=0
    count = 1
    
    while limit > 0:
        count = str(count*2)
        if len(count)>10:
            count = int(count[-10:])
        else:
            count = int(count)
        limit-=1
    
    count = str(count*28433)
    if len(count)>10:
        count = int(count[-10:])
    else:
        count = int(count)
    count+=1
    
    time_end = time()
    print "Answer:", count
    print "Time taken", time_end-time_start
