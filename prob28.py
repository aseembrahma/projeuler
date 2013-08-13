import sys
from time import time


if __name__ == "__main__":
    time_start = time()
    total = 1
    limit = 1001
    current_square_length = 1
    square_length_increment = 2
    current_number = 1
    while current_square_length != limit:
        for i in range(4):
            current_number += current_square_length
            current_number += 1
            total+=current_number
        current_square_length = current_square_length + square_length_increment
    print "Answer:", total
    time_end = time()
    print "Time taken", time_end-time_start
