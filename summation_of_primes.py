from math import sqrt,ceil

# Problem 10: Summation of Primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# TODO: implement Sieve of Eratosthenes algorithm for a higher performance algorithm.
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def isPrime(prime):
	for x in range(2,int(ceil(sqrt(prime)))+ 1):
		if prime % x == 0:
			return False
	return True

def totalPrimeSum(k):
	summation = 2
	for x in range(3,k,2):
		if isPrime(x):
			summation = summation + x
	return summation

def main():
	k=2000000
	total_sum = totalPrimeSum(k)
	print str(total_sum) + " is the total sum of primes under " + str(k)

if __name__=="__main__":
	main()