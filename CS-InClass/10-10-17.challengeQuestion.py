import sys

import random


num = []
squares = []
z = int(input('How many numbers do you want to sort?'))

for i in range(0,z):
	num.append(random.randint(0,100))
for t in range(0,len(num - 1)):
	if num[t]**(0.5)%1 == 0