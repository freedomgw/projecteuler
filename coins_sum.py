# problem 31: coin sums
# dynamic programming

coins=[1,2,5,10,20,50,100,200]
ways=[[1,1,1,1,1,1,1]]

def findCoinSum(target):
	row=[]
	coinCurrentTarget=2
	while coinCurrentTarget != 201:
		row.append(1)
		for x in range(1,8):
			if coinCurrentTarget == coins[x]:
				row.append(row[x-1] + 1)
			elif coinCurrentTarget > coins[x]:
				remainder = coinCurrentTarget - coins[x]
				remainder_ways = ways[remainder-1][x]
				row.append(remainder_ways + row[x-1])
			else:
				row.append(row[x-1])
		ways.append(row)
		row=[]
		coinCurrentTarget = coinCurrentTarget + 1
	return ways[199][7]

def main():
	target = 200
	total_ways = findCoinSum(200)
	print("total ways: " + str(total_ways))

if __name__ == "__main__":
	main()