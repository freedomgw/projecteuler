from math import sqrt, ceil

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?
# 104743

def find10001PrimeNumber():
	primeFoundSoFar=1
	primeNumber=2
	primePotential=primeNumber
	while True:
		for x in range(2,ceil(sqrt(primePotential)) + 1):
			if primePotential % x == 0:
				break
			elif x == int(ceil(sqrt(primePotential))):
				primeFoundSoFar = primeFoundSoFar + 1
				primeNumber = primePotential
				if primeFoundSoFar==10001:
					return primeNumber
		primePotential = primePotential + 1

def main():
	primeNumber = find10001PrimeNumber()
	print("primeNumber found: " + str(primeNumber))

if __name__ == "__main__":
    main()