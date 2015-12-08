# Problem 5: Smallest Multiple
def result():
	k=[11,12,13,14,15,16,17,18,19,20]
	value = 20
	while True:
		smallest_multiple = True
		for test_multiple in k:
			remainder = value % test_multiple
			if remainder != 0:
				value += 20
				print value
				break
			elif remainder == 0 and test_multiple == 20:
				return value

def main():
	print result()

if __name__=="__main__":
	main()
