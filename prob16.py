import sys
import math

def compute_power(x, n):
	if n == 0:
		return 1
	elif n % 2 == 0:
		return math.pow(compute_power(x, n/2), 2)
	elif n % 2 == 1:
		return x * math.pow(compute_power(x, (n-1)/2), 2)

def sum_digits(num):
	sum = 0
	while num > 0:
		sum = sum + num % 10
		num = math.floor(num / 10)
		print num
	return sum

def old_main():
	value = compute_power(2, 1000)
	print "Answer:", sum_digits(math.pow(2,1000))

def main():
    digits = [1]
    power = 1000
    carry = False
    while power > 0:
        for i in range(len(digits)):
            digits[i] = digits[i] * 2
            if carry:
                digits[i] = digits[i] + 1
                carry = False
            if digits[i] >= 10:
                digits[i] = digits[i] - 10
                carry = True
        if carry:
            digits.append(1)
            carry = False
        power = power - 1
    print sum(digits)

if __name__ == "__main__":
    main()