# Problem 9: Special Pythagorean triplet
import math

def get_all_permutations():
	permutation = []
	for a in range(1, 2500):
		for b in range(1, 2500):
			left_side = pow(a,2) + pow(b,2)
			if math.sqrt(left_side) % 1 == 0:
				permutation.append([a, b, int(math.sqrt(left_side))])
	return permutation

def special_pytha_triplet():
	for permutation in get_all_permutations():
		if (permutation[0] + permutation[1] + permutation[2]) == 1000:
			print permutation[0] * permutation[1] * permutation[2]

def main():
	special_pytha_triplet()

if __name__=="__main__":
	main()
