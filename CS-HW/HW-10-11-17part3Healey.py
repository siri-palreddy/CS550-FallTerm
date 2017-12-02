import sys
import random


#Generate a list of 10 random numbers between 0, 100

randNums = list()

for i in range(10):
    (randNums.append(random.randint(0, 100)))


#Get them in order
randNums.sort()
#print('The List of random numbers after sorting:\n',randNums)

for randNum in randNums:
    if (randNum%3 == 0):
        randNums.remove(randNum)

print('The List of random numbers:\n',randNums)