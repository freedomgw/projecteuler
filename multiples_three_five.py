k=1000
sum=0
for x in range(0,k):
	if x % 3 == 0 or x % 5 == 0:
		sum = sum + x
print sum
