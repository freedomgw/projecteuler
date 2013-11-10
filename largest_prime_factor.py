# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# answer: 6857
# computation of 12.4074430466 seconds

from math import sqrt,ceil
import time

def isPrime(prime):
	if prime == 2:
		return True
	for x in range(2,int(ceil(sqrt(prime)))+ 1):
		if prime % x == 0:
			return False
	return True

def findLargestPrime(k):
	for x in range(int(ceil(sqrt(k)))+ 1,-1,-1):
		if isPrime(x):
			if k % x == 0:
				return x

def main():
	start = time.time()
	k=600851475143
	largest = findLargestPrime(k)
	print str(largest) + " is the largest prime found for " + str(k)
	print 'It took', time.time()-start, 'seconds.'

if __name__=="__main__":
	main()
