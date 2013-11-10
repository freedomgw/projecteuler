# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# answer: 6857
# computation of 8.92887496948 seconds

from math import sqrt,ceil
import time

def isPrime(prime):
	for x in range(2,int(ceil(sqrt(prime)))+ 1):
		if prime % x == 0:
			return False
	return True

def findLargestPrime(k):
	rootk = int(ceil(sqrt(k)))
	if rootk % 2 == 0:
		rootk = rootk - 1
	for x in range(rootk,-1,-2):
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
