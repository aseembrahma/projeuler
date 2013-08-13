b_list = range(499, 0, -1)
a_list = range(499, 0, -1)


for a in a_list:
	for b in b_list:
		c = 500 - ((a*b)/1000)
		#if a+b == 500 + (a*b)/1000:
		#	print "found2:", a, b
		
		if c > a and c > b:
			if c*c == a*a + b*b:
				print "found:", a, b, c, (a*b*c)
