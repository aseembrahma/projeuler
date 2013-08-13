import sys
from time import time


if __name__ == "__main__":
    time_start = time()
    total = 1
    limit = 1000000
    
    import itertools
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    all_permutations = itertools.permutations(numbers)
    i = 0
    while i != limit:
        total=all_permutations.next()
        i+=1
    print "Answer:", total
    time_end = time()
    print "Time taken", time_end-time_start
