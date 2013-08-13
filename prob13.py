import sys

def main():
	fp = open(sys.argv[1], "r")
	contents = fp.read().split("\n")
	num_rows = len(contents)
	num_cols = len(contents[0])
	#print "num rows", num_rows, "num cols", num_cols
	
	sum = []
	carry_over = 0
	
	for i in range(num_cols-1, -1, -1):
		col_sum = 0
		for j in range(num_rows):
			#print "row", j, "col", i
			col_sum = col_sum + int(contents[j][i])
		col_sum = col_sum + carry_over
		sum.append(col_sum % 10)
		carry_over = int(col_sum / 10)
	
	if not carry_over == 0:
		sum.append(carry_over)
	sum.reverse()
	print "Answer:", "".join(["%d" % x for x in sum])

if __name__ == "__main__":
    main()