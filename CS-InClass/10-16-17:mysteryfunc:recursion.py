import sys

n = int(input('Please enter an integer to go through the mystery function: '))

sepList = [int(i) for i in str(n)]
print(sepList)


def mystery(sepList):
	return(sum(sepList))
	
print(mystery(sepList))

