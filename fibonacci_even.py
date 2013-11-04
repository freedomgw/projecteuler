sum=2
fib=[1,2,0]
while True:
	if fib[2] > 4000000:
		break
	fib[2]=fib[0]+fib[1]
	if fib[2]%2==0:
		sum=fib[2]+sum
	fib[0]=fib[1]
	fib[1]=fib[2]
print sum
