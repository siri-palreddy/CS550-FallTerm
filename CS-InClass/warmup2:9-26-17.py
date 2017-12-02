import sys

n = int(input('Please enter an integer value: '))
a = 1
b = 1
while a>=1 and b>=1:
	print(a)
	temp = a + b
	a = temp + b
	print(a)