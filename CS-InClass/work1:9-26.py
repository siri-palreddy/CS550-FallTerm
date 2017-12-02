import sys

n = int(input('Please enter an integer: '))

for a in range(n):
	if (a <= n and a%8 == 0):
		print(a)