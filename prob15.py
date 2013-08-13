import sys

def factorial(num):
	return reduce(lambda x, y:x*y, range(1, num+1))
	
def main():
	temp = factorial(20)
	print factorial(40)/(temp*temp)

if __name__ == "__main__":
    main()