
def palindrome(number):
	test = str(number)
	return (test == test[::-1])

maxnum = 0
for i in range(999, 99, -1):
	for j in range(i-1, 99, -1):
		if palindrome(i * j):
			maxnum = max(maxnum, i*j)
print maxnum