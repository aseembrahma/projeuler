limit = 100000
primes = range(2, limit)
i = 0
total_sum = 0

while i < len(primes):
	j = i+1
	while j < len(primes):
		if primes[j] % primes[i] == 0:
			primes.pop(j)
		else:
			j = j + 1
	total_sum = total_sum + primes[i]
	i = i + 1

print total_sum
