import sys
from time import time

if __name__ == "__main__":
    time_start = time()
    
    filename = "triangle.txt"
    contents = [map(lambda y: int(y.strip()),x.split(" ")) for x in open(filename).read().split('\n') if len(x)>0]
    #from copy import copy
    #sums = copy(contents)
    
    for i in range(len(contents)-2, -1, -1):
        for j in range(len(contents[i])):
            # update row i's values based on the values of row i+1
            contents[i][j] += max(contents[i+1][j], contents[i+1][j+1])
    
    print "Answer:", contents[0][0]
    time_end = time()
    print "Time taken", time_end-time_start
