import math

def find_closest_triangle(some_num):
	i = 1
	temp = (i*(i+1))/2
	while (temp < some_num):
		i = i + 1
		temp = (i*(i+1))/2
	return i

def count_divisors(some_num):
	if some_num == 1:
		return 1
	max_divisor = int(math.sqrt(some_num))
	num_divisors = 0
	for i in range(1, max_divisor+1):
		if some_num % i == 0:
			num_divisors = num_divisors + 2
	return num_divisors

def main():
	num = 250*251
	i = find_closest_triangle(num)
	temp = (i*(i+1))/2
	while count_divisors(temp) < 500:
		i = i + 1
		temp = (i*(i+1))/2
	print "Answer:", temp

if __name__ == "__main__":
    main()