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