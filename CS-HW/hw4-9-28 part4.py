import sys
import math
import random

tot = int(input("Please enter the number of times you are flipping the coin: "))
hc = 0
tc = 0
for i in range(0,tot):
	coinResult = random.randrange(0,2)
	##print(coinResult)
	if (coinResult == 1):
		hc += 1
	else:
		tc += 1
print("Number of heads is: ", hc)
print("Percentage of heads is: ", ((hc*100)/tot))

##heads = tot - tails
##print("Number of heads: ", heads, "Percentage of heads: ", (heads*100)/tot)
