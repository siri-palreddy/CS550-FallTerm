import sys
import math

x1 = int(input('Please enter the x coordinate of your first point: '))
y1 = int(input('Please enter the y coordinate of your first point: '))
x2 = int(input('Please enter the x coordinate of your second point: '))
y2 = int(input('Please enter the y coordinate of your second point: '))

##def square(x):
	##return x*x
##def distance(x1, y1, x2, y2)
	##return math.sqrt((x2 - x1)*2 + (y2 - y1)*2)

answer = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('Here is the distance between these points: ', answer, ' units')