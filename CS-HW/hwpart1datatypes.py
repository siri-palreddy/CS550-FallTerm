import sys
## t= temperature in Fahrenheit
## v= wind speed in miles per hour
## w= wind chill
t = float(sys.argv[1])
v = float(sys.argv[2])


w = 35.74 + (0.6215 * t) + (0.4275 * t - 35.75) *  (v ** 0.16)
print ('Wind Chill:',w)
/Users/spalreddy20/Desktop/guessinggame.py
