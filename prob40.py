import sys
from time import time

def digit_combinations(nth, n):
    return nth+int('1'+'0'*(n-1))

def digit_possibilities(n):
    return 9*pow(10, n-1)

def brute_check(n):
    temp=0
    tempstr=''
    while len(tempstr)<n:
        temp+=1
        tempstr+=str(temp)
    print tempstr
    print len(tempstr)
    return int(tempstr[n-1])

if __name__ == "__main__":
    time_start = time()
    limit = 1000000
    limit_lower = 1
    total=1
    required_digits = [1, 10, 100, 1000, 10000, 100000, 1000000]#1000: 370
    #required_digits = [1,2,3,4,5,10, 15]
    values = []
    # 0.123456789101112131415161718192021...
    
    num_digits = 0
    total_length = 0
    while len(required_digits)>0:
        if required_digits[0] > total_length and required_digits[0] <= total_length + ((num_digits+1)*digit_possibilities(num_digits+1)):
            temp=required_digits[0]-total_length-1
            digit_combination = digit_combinations(temp/(num_digits+1), num_digits+1)
            print "debug", required_digits[0], temp, digit_combination
            values.append(int(str(digit_combination)[temp%(num_digits+1)]))
            del required_digits[0]
        else:
            num_digits+=1
            total_length+=(num_digits*digit_possibilities(num_digits))
    print "values", values
    print "Answer:", reduce(lambda x, y: x*y, values)
    time_end = time()
    print "Time taken", time_end-time_start
