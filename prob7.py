primes = []

def isprime(number):
	for num in primes:
		if number % num == 0:
			return False
	primes.append(number)
	return True

limit = 10001
i = 2
while len(primes) < limit:
	isprime(i)
	i = i+1
print primes[-1]
