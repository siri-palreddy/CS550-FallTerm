# Siri Palreddy, 10-5-17
# This game is an adventure game. The user first picks their own character, and from there,
# goes through a series of obstacles in "The Temple of Doom". If they fail at an obstacle,
# they must start over. In the end, if you get through everything, you receive a mystical reward.
# Sources: www.python.org
# On my honor, Siri Palreddy
import sys
import random

print('Enter at your own risk... ',) #Opening statement

print('Choose your character. Your options are: ') #Gives options/descriptions of characters
AS = ('Auburn Sally - The feared female captain of The Dolly Llama, who roams the      Caribbean with her all-women crew.')
BV = ('Beau Vandenbuke - The youngest and most accomplished archaeologist in the world,who travels in his blimp to find adventure.')
GQ = ('Galaxy Queen - The cyborg ruler of the universe, who visits distant planets in  her spaceship with an army of robots and mutants.')
BT = ('Bolt Thunder - A kid superhero who draws his power from electricity. He lives   with his family of superheroes, saving the world one day at a time.')
ASN = ('Auburn Sally')
BVN = ('Beau Vandenbuke')
GQN = ('Galaxy Queen')
BTN = ('Bolt Thunder')
# character = GQN
print(AS) #print the descriptions
print(BV)
print(GQ)
print(BT)
choice = input('Whom do you choose? ')

def characterChoice(choice): #The function simplifies the purpose, so that the code easily rejects an invalid input.
	while (choice not in (ASN, BVN, GQN, BTN)):
		print('That\'s an interesting choice, but please select from our list of characters and type in the name exactly as shown.')
		choice = input('Whom do you choose? ')
	else:
		return(choice)
print('Welcome to your adventure ' + characterChoice(choice)) #If the character choice is valid, the function is called back to a line of text.
#print(characterChoice(choice))
	

def getMessage(messageID): #Function keeps all the intro messages in one place. Then returns message when I call it with a number.
	msg = ''
	if messageID == 1:
		msg  = 'You are in the Temple of Doom. Your first obstacle is ahead: '
	if messageID == 2:
		msg = 'There is a chasm between you and the other side of the temple.\nFortunately, a tiled bridge connects the sides. However, only one tile out of   the ten will get you across safely.\nEach tile is numbered from 1-10.\nGuess the number of the safe tile and you will live a little longer...'
	if messageID == 4:
		msg = 'The danger is not done. A large, snarling dragon has crossed paths with you.\nThe only way through is to answer her series of riddles...'
	if messageID == 3:
		msg = ('\nYou have come far, ' + characterChoice(choice) + '. The Oracle honors you with your choice of      rewards. Your options are: ')
	return(msg)


def getNumber(): #This function simplifies the guessing game, basically covering whenever an input is not valid. A loop makes sure that someone must enter an actial number.
	isNumber = False
	while isNumber == False:
		try:
			c = int(input('Enter a number from one to ten. You have three tries.'))
			isNumber = True
		except:
			print('Please enter a whole number from 1 to 10.')
	return c

print(getMessage(1)) #This is calling back the getMessage function with the introduction.
def get_dir(): #This is the first obstacle, creating a function that is later called.
     validDirections = ["NORTH", "SOUTH", "EAST", "WEST"] #These are valid directions that can be entered.
     direction = input("You first come to an intersection. Which way will you go? : \nWest\nEast\nSouth\nNorth\n:").upper() #This is my input. The .upper lets me compare the capitalized version of the answer to the directions.
     while direction not in validDirections:
         direction = input("Please enter a valid direction. ").upper()
     badDirection = validDirections[random.randint(0, 3)] #This gives the user a 75% chance of getting correct path.
     if (direction == badDirection): #If the incorrect answer is entered, I set the direction as QUIT, which is later referenced.
         print('You chose a wrong path - You are dead. Choose wisely next time!')
         direction = "QUIT"
     else:
     	print('You chose the safe direction: ' + direction + '. The Oracle allows you to pass.') #Lets the user through with right direction.
     return direction
if (get_dir() == "QUIT"): #So when the direction is wrong, it will equal QUIT. When the function is called back with QUIT, you are exited out of the program.
   	exit()


print(getMessage(2)) #This goes back to the getMessage function, putting the second introduction.
y = random.randrange(1,11)


rightGuess = False #This is a more complicated version of our first guessing game, giving the user only three tries.
tries = 0
while tries < s3: #When you have not used all your tries, the guessing system will work, telling you if you are too high or low.
	userNum = getNumber()
	tries += 1
	if userNum > y:
		print('Too high! Guess again!')
	elif userNum < y:
		print('Too low! Guess again!')
	else:
		rightGuess = True #When guess is correct, you pass on.
		print('You have gained the Oracle\'s approval. You may pass.')
		break
if not(rightGuess): #When the tries are used, the program exits.
	print('You have lost your chances: Play again!')
	exit()

print(getMessage(4)) #Printing message from my getMessage function
def Riddle1():
	print('Your first riddle is:')
	e = input('Poor people have it. Rich people need it. If you eat this, you shall die... You have five tries.').upper()
	R1ans = 'NOTHING' #Correct Answer
	attempts = 0
	while e not in R1ans and attempts < 5:#Let user have 5 chances
		attempts += 1
		e = input('This is not a correct type of answer. Try again.')#When input is wrong
	if e != 'NOTHING' and attempts >= 5:
		print('You lost all your chances and irritated the dragon. You are now in its stomach.')
		exit()
	else:
		print('You solved the first riddle- The dragon has let you through.')#When answer is right.
	

Riddle1() #Runs function

def Riddle2(): #Same as above riddle
	print('Your second riddle is:')
	f = input('What occurs once in a minute, twice in a moment, and never in a thousand years?. You have five tries.').upper()
	R2ans = 'M'
	attempts = 0
	while f not in R2ans and attempts < 5:
		attempts += 1
		f = input('This is not a correct type of answer. Try again.')
	if f != 'M' and attempts >= 5:
		print('You lost all your chances and irritated the dragon. You are now in its stomach.')
		exit()
	else:
		print('You solved the second riddle- The dragon has let you through.')
Riddle2()

def Riddle3(): #Same as above
	print('Your third riddle is:')
	g = input('What gets sweeter as it grows older?... You have five tries.').upper()
	R3ans = 'WINE'
	attempts = 0
	while g not in R3ans and attempts < 5:
		attempts += 1
		g = input('This is not a correct type of answer. Try again.')
	if g != 'WINE' and attempts >= 5:
		print('You lost all your chances and irritated the dragon. You are now in its stomach.')
		exit()
	else:
		print('You solved the last riddle- The dragon has let you through.')
Riddle3()

print(getMessage(3)) #Printing the message from my getMessage function when inputting 3.
RN = '\nHeart of the Ocean:\nA large, heart-shaped ruby pendant necklace, stolen from the most terrible      vagabond alive. They say incredible powers come with it, but none have ever\nexperienced it before.'
LG = '\nCandypopigilist:\nYour own personal planet made entirely out of candy, with a resort included.'
HS = '\nHand of the Sun:\nAn ancient gold relic that allows you to travel through time at your beck and   call.'
BV = '\nSmart Sip:\nA potion that renders you the most knowledgeable person of this world. But be   careful- this knowledge comes with a price...'
RNN = 'Heart of the Ocean'
LGN = 'Candypopigilist'
HSN = 'Hand of the Sun'
BVN = 'Smart Sip'


print(RN)
print(LG)
print(HS)
print(BV)
prizee = input('What do you choose? ')
def prizeChoice(prizee): #The function simplifies the purpose, so that the code easily rejects an invalid input.
	while (prizee not in (RNN, LGN, HSN, BVN)):
		print('That\'s an interesting choice, but please select a prize from here.')
		prizee = input('\nWhat do you choose? ')
	else:
		return(prizee)
print('Enjoy your ' + prizeChoice(prizee) + ', ' + characterChoice(choice) + '... while you can...') #Prints the prize choice along with previous global code of the user's character name.
print('Play again!')
exit() 


