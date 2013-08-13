import sys
from copy import copy
from time import time, sleep
from math import sqrt, floor, ceil

#answer = 73682
required_total = 200
denominations = [200, 100, 50, 20, 10, 5, 2, 1]
#max_values = [(required_total/x) for x in denominations]
max_values = [1, 2, 4, 10, 20, 40, 100, 200]
total = 0
debug = 0

def p_value(s):
    if len(s) != len(denominations):
        print "ERROR"
        sys.exit(1)
    return sum([denominations[x]*s[x] for x in range(len(s))])

def branching_out(value_list_orig, value_remaining, spaces):
    global total
    
    value_list = copy(value_list_orig)
    if debug: print "checking", value_list, value_remaining, spaces
    for i in range(0, (value_remaining/denominations[spaces])+1):
        #value_list[spaces]+=(i/denominations[spaces])
        #value_remaining-=denominations[spaces]
        value_list[spaces]=i
        value_remaining=required_total-p_value(value_list)
        if debug: print "i", i, value_remaining, spaces
        if value_remaining == 0:
            total += 1
            if debug: print "found"
            #print value_list
            break
        elif value_remaining < 0:
            break
        if spaces>0 and value_remaining >= denominations[spaces-1]:
            branching_out(value_list, value_remaining, spaces-1)
    if debug: print "returning"

if __name__ == "__main__":
    time_start = time()
    limit = 1000
    limit_lower = 0
    total = 0
    
    branching_out([0, 0, 0, 0, 0, 0, 0, 0], 200, 7)
    """
    current_values = [0 for x in range(len(denominations))]
    addition = 1
    while current_values[0]!=max_values[0]:
        
        position = len(denominations)-1
        while addition>0:
            current_values[position] = current_values[position] + 1
            if current_values[position] > max_values[position]:
                current_values[position] = 0
                position-=1
            else:
                addition-=1
        #print current_values
        pval = p_value(current_values)
        if pval==required_total:
            total+=1
            #print "found"
            addition = 1
        elif pval > required_total:
            addition = (max_values[-1]-current_values[-1])+1
        else:
            addition = 1
    """
    time_end = time()
    print "Answer:", total
    print "Time taken", time_end-time_start
