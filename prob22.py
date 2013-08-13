import sys
from time import time


if __name__ == "__main__":
    time_start = time()
    contents=[x.strip('"') for x in open("names.txt").read().split(",")]
    contents.sort()
    total=0
    for i in range(len(contents)):
        s=contents[i]
        score=sum([(ord(x)-ord('A')+1) for x in s])
        total+=((i+1)*score)
    print "Answer:", total
    time_end = time()
    print "Time taken", time_end-time_start
