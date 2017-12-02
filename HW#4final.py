(1)
import sys
import math

## t= temperature in Fahrenheit
## v= wind speed in miles per hour
## w= wind chill
t = float(sys.argv[1])
v = float(sys.argv[2])

if math.fabs(t) > 50:
	print("Error: t should be greater than -50 and less than 50.")
	exit()
if (v > 120 or v < 3):
	print("Error: v should be greater than 3 and less than 120.")
	exit()
w = 35.74 + (0.6215 * t) + (0.4275 * t - 35.75) *  (v ** 0.16)
print ('Wind Chill: ',w)

##----------------------------------------------------------------------------------------------------
(2)
import sys


for n in range(1000,2000):
	if (n%5 == 0):
		print(n, n+1, n+2, n+3, n+4)

##----------------------------------------------------------------------------------------------------
(3)
##HW Part 3:
## Explain the code's output.
## Both f and g output to the fibonacci sequence, except, f starts with 1, while g starts with 0,
## and f ends with 987, and g ends at 610. For clarification, I tried out this code.

##----------------------------------------------------------------------------------------------------
(4)
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
##----------------------------------------------------------------------------------------------------
##Output for question 4:
## tot = 10: Number of heads is:  5
			 ##Percentage of heads is:  50.0

## tot = 100: Number of heads is:  52
			 ##Percentage of heads is:  52.0

## tot = 1000: Number of heads is:  501
			 ##Percentage of heads is:  50.1

## tot = 10000: Number of heads is:  5026
			 ##Percentage of heads is:  50.26

## tot = 100000: Number of heads is:  49863
			 ##Percentage of heads is:  49.863

## tot = 1000000: Number of heads is:  500064
			 ##Percentage of heads is:  50.0064

## As you can see, there is a pattern to the outputs: all are near the value of 50.
## This shows that even a computer's randomness will generate a patter, and therefore,
## codes that rely on randomness can potentially be hacked. As a sample gets larger, there
## is an easier pattern to see, and randomness decreases in data.


