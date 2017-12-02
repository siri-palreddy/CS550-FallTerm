import sys
import random
play = 'Yes'

while play == 'Yes':
	x = int(input('Enter a number between 0 and 100: '))
	print(x)
	y = random.randrange(0,100)

	while x != y:
		if x > y:
			print('Too high! Guess again!')
		elif x < y:
			print('Too low! Guess again!')


		x = int(input('Guess again: '))

	play = input('You win! Way to go! Would you like to play again? ')

	

print('Ok, bye then!')