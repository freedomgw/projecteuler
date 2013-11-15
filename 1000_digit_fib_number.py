# http://projecteuler.net/problem=25
term = 3
fib=[1,2,0]
while True:
	fib[2]=fib[0]+fib[1]
	if fib[2]%2==0:
		if len(str(fib[2])) >= 1000:
			term = term + 1
			print str(term)
			# print str(fib[2])
			break
	fib[0]=fib[1]
	fib[1]=fib[2]
	term = term + 1