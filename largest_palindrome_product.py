# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# this functions assumes that a palindrome has already been processed and processes
# the next palindrome
def createNextLargestPalindrome(k):
	strPalinLen=int(len(str(k))/2)
	stringPalindrome=str((int(k/(10**(strPalinLen)))-1))
	# possibly one less digit afterwards
	strPalinLen=len(str(stringPalindrome))
	strLen=len(str(stringPalindrome))
	currentPalinLen=strPalinLen-1
	while currentPalinLen != -1:
		stringPalindrome=stringPalindrome+stringPalindrome[currentPalinLen]
		currentPalinLen=currentPalinLen-1
	return int(stringPalindrome)

def findProduct(palindrome):
	product1=1
	product2=999
	temp=None
	while len(str(product2))==3:
		# print "palindrome being investigated: " + str(palindrome)
		# print "product2: " + str(product2)
		if palindrome % product2 == 0:
			product1 = int(palindrome / product2)
			if len(str(product1))==3 and len(str(product2))==3:
				# print ("product1: " + str(product1))
				# print ("product2: " + str(product2))
				return palindrome
		product2 = product2 - 1
	return -1

def main():
	k=999*999
	minimumLimit=100*100
	while k >= minimumLimit:
	    k=createNextLargestPalindrome(k)
	    foundPalindrome = findProduct(k)
	    if foundPalindrome != -1:
	    	print foundPalindrome
	    	return 0

if __name__ == "__main__":
    main()