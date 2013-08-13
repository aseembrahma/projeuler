import sys
from time import time

if __name__ == "__main__":
    time_start = time()
    limit = 10000
    limit_lower = 0
    total=0
    count = 1
    
    all_nums = [True for x in range(1, limit)]
    for i in xrange(1, limit):
        if all_nums[i-1]==False:
            continue
        
        templist=[i]
        for j in range(1, 50+1):
            temp = templist[-1]+int(str(templist[-1])[::-1])
            if str(temp)==str(temp)[::-1]:
                for k in templist:
                    if k < limit:
                        all_nums[k-1] = False
                break
            else:
                templist.append(temp)
    time_end = time()
    print "Answer:", all_nums.count(True)
    print "Time taken", time_end-time_start
