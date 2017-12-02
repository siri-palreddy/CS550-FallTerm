import random

# Ask for number of random numbers the user wants to generate 
z = int(input("How many numbers do you want to generate? "))

# Create empty lists: 'num' for generated random numbers, 'squares' for perfect squares pulled from 'num'
num = []
squares = []

# Generate z number of random numbers and add them to 'num' as they're generated
for i in range (0, z):
	num.append(random.randint(0, 100))

# Print the full list of random numbers for testing purposes
print("Full list: " + str(num))

# Go through each number in 'num' and check to see if it is a perfect square
for t in range (1, len(num)):
	if (num[t-1] ** 0.5)%1 == 0:  # If the square root has no remainder when divided by 1 (aka "is it a whole number?")
			squares.append(num[t-1])	# add the number being tested to the 'squares' list
			num.remove(num[t-1]) 		# and remove it from the original list
 
# Print the final list of squares
if len(squares) == 0: 	# If no perfect squares were found and added to 'squares' (aka "is the list 'squares' empty?")
	print("Squares: None")   # print "none"

else:
	print("Squares: " + str(squares)) # Print the final list of squares


