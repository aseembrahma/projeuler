limit = 100
sum = 0
for i in range(1,limit+1):
	for j in range(i+1, limit+1):
		sum += i*j
print 2*sum