import sys

letters_basic = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', ]

letters_middle = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', ]

letters_tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', ]

def main():
	sum_less_than_hundred = sum(map(len, letters_basic)) + sum(map(len, letters_middle)) + sum(map(len, letters_basic)) * len(letters_tens) + sum(map(len, letters_tens)) * (len(letters_basic)+1)
	
	sum_temp = (100*sum(map(len, letters_basic))) + (9*100*len('hundred')) + (9*99*len('and')) + (9*sum_less_than_hundred)

	sum_total = sum_less_than_hundred + sum_temp + len('one')+len('thousand')
	print "Answer:", sum_total
	

if __name__ == "__main__":
    main()