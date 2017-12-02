import sys

n = int(input('Enter a number: '))

if n%11 == 0 or n%11 == 1:
	print('This number is SPECIAL!!!')
else:
	print('This number is not special.')