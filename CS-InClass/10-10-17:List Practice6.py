import sys


listColors = ['red', 'blue', 'green']


for i in range(len(listColors)):
	if listColors[-1] == 'green':
		listColors[-1] = 'cyan'
print(listColors)