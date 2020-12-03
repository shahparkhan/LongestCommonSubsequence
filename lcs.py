##########################################
########LONGEST COMMON SUBSEQUENCE########
##########################################


#object to store cost and direction with update functions
class obj:
	def __init__(self, cost):
		self.cost = cost
		self.direction = ""

	def update_cost(self, cost):
		self.cost = cost

	def update_direction(self, direction):
		self.direction = direction


#function to update costs and direction in the 2D array
def update_array(array, string1, string2, len1, len2):
	
	#traversing 2D array and making updates
	for i in range(1, len2+1):
		for j in range(1, len1+1):

			#if chars match, adding one to cost
			if string1[j-1] == string2[i-1]:
				cost = 1 + array[i-1][j-1].cost
				array[i][j].update_cost(cost)
				array[i][j].update_direction("northeast")

			#otherwise carrying for maximum of either north or east cost
			else:
				
				if array[i-1][j].cost >= array[i][j-1].cost:
					cost = array[i-1][j].cost
					array[i][j].update_cost(cost)
					array[i][j].update_direction("north")
				
				else:
					cost = array[i][j-1].cost
					array[i][j].update_cost(cost)
					array[i][j].update_direction("east")

	return array

#function to traverse the 2D array and extract a valid longest common subsequence
def get_lcs(array, string1, string2, len1, len2):
	
	#initialzation
	result = ""

	i = len2
	j = len1

	#loop in array from bottom right and traversing in a northeast direction
	#subsequently concatenating valid chars to resultant string
	while ((i != 0) and (j != 0)):
		
		#add char
		if array[i][j].direction == "northeast":
			result = string2[i-1] + result
			i = i - 1
			j = j - 1

		#move north
		elif array[i][j].direction == "north":
			i = i - 1

		#move east
		else:
			j = j - 1

	return result


#function to find longest common subsequence
def lcs(string1, string2):
	#finding lengths of input string
	len1 = len(string1)
	len2 = len(string2)

	#making 2D array
	row = [obj(0)]*(len1+1)
	array = []

	for i in range(len2+1):
		row = [obj(0) for i in range(len1+1)]
		array.append(row)

	#updating array 
	array = update_array(array, string1, string2, len1, len2)

	#getting subsequence
	result = get_lcs(array, string1, string2, len1, len2)

	return result

def main():
	print("Longess Common Subsequence\n")
	
	string1 = input("Enter first string: ")

	string2 = input("Enter second string: ")

	LCS = lcs(string1, string2)

	print("\nLongest common subsequence is:", LCS)


if __name__ == "__main__":
	main()