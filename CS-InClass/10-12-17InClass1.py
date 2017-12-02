import sys
import random

#name = input('What is your first name? ')
#form = int(input('What form are you in? '))
#age = int(input('How old are you? '))
#dorm = input('What dorm, or town, do you live in?')
def ask():
	name = input('What is your first name? ')
	form = int(input('What form are you in? '))
	age = int(input('How old are you? '))
	dorm = input('What dorm, or town, do you live in?')

n = []

for i in range (3):
	row = [0.0]*4
	row[0] = input('What is your first name? ')
	row[1] = int(input('What form are you in? '))
	row[2] = int(input('How old are you? '))
	row[3] = input('What dorm, or town, do you live in?')
	n.append(row)
	
print('Poll: ', n)
