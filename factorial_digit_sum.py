from math import factorial

def factorialDigitSum(k):
	factsum=0
	k=factorial(k)
	length=len(str(k))-1
	for x in range(length,0,-1):
		divide = int(k/(10**x))
		digits = len(str(divide))
		if digits == 1:
			digit = divide
		else:
			digit = divide - ((int((divide/10))) * 10)
		factsum=factsum+digit
	return factsum

def main():
	k=100
	factorial_sum = factorialDigitSum(k)
	print("factorial_sum: " + str(factorial_sum))

if __name__ == "__main__":
    main()