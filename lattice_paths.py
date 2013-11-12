# Problem 15: Lattice paths
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# Recursion

# def permuteRoutes(x,y):
# 	print "x: " + str(x) + ", y: " + str(y)
# 	if x == 20 and y == 20:
# 		return 1
# 	if x < 20 and y < 20:
# 		return permuteRoutes(x+1, y) + permuteRoutes(x, y+1)
# 	elif x == 20:
# 		return permuteRoutes(x,y+1)
# 	elif y == 20:
# 		return permuteRoutes(x+1,y)

# Dynamic Programming
# Big O(n^2) analysis

def findTotalRoutes(n):
	# 2D array
	routes=[]
	current_row=[]
	for x in range(0,n):
		current_row.append(1)
	routes.append(current_row)
	for row in range(1,n):
		for x in range(0,n):
			if x == 0:
				current_row[x] = 1
			else:
				current_row[x] = routes[row-1][x] + current_row[x-1]
		routes.append(current_row)
	return routes[n-1][n-1]

def main():
	routes = findTotalRoutes(21)
	print("total routes: " + str(routes))

if __name__ == "__main__":
	main()