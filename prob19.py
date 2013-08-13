import sys

def is_leap_year(year):
	return year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)

def days_in_year(year):
	return (year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)) and sum(days_leap) or sum(days)

def num_sundays(first, year):
	return 1 + (days_in_year(year) - first)/7

def num_sundays_first(first, year):
	days_list = is_leap_year(year) and days_leap or days
	sum = 0
	for month_days in days_list:
		if first == 1:
			sum = sum + 1
		first = 7 - ((month_days - first) % 7)
	return sum

def next_sunday_year(first, year):
	upper = days_in_year(year)
	return 7 - ((upper - first) % 7)

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def main():
	sum_total = 0
	first = 7
	for year in range(1901, 2001):
		first = next_sunday_year(first, year - 1)
		temp = num_sundays_first(first, year)
		sum_total = sum_total + temp
	print "Answer:", sum_total
	

if __name__ == "__main__":
    main()