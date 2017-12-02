import sys
import random
import math


def getRow(cellNumber):
	rowNumber = math.ceil(cellNumber/totalColumns)
	return rowNumber
def getColumn(cellNumber):
	columnNumber = cellNumber%totalColumns
	if columnNumber == 0:
		columnNumber = totalColumns
	return columnNumber


try:
	totalRows = int(input('How many rows would you like?'))
	totalColumns = int(input('How many columns would you like?'))
	mines = int(input('How many mines would you like?'))
except ValueError:
	print('Please enter valid numbers. Don\'t trick me!')
	exit()

totalCells = totalRows * totalColumns
# print(totalRows, totalColumns, mines)
if mines > (totalCells/10):
	print('You cannot have more than 10 percent of your cells as mines.')
	exit()



mineBoard = [[0 for x in range(totalColumns)] for x in range(totalRows)]



randMines = list()
for i in range(mines):
    mineLocation = random.randint(1, (totalCells + 1))
    # To avoid duplicate mines
    while (mineLocation in randMines):
        mineLocation = random.randint(1, (totalCells + 1))
    randMines.append(mineLocation)

for i in range(totalRows):
    print(mineBoard[i])
print (randMines)


for i in randMines: # As index starts with zero we need to adjust the index
	mineRow = getRow(i) - 1
	mineColumn = getColumn(i) - 1
	print(mineRow)
	print(mineColumn)
	mineBoard[mineRow][mineColumn] = 100
	
	if (mineRow > 0):
		mineBoard[mineRow - 1][mineColumn] += 1
		if (mineColumn > 0):
			mineBoard[mineRow - 1][mineColumn - 1] += 1
		if (mineColumn < (totalColumns - 1)):
			mineBoard[mineRow - 1][mineColumn + 1] += 1
	
	if (mineRow < (totalRows - 1)):
		mineBoard[mineRow + 1][mineColumn] += 1
		if (mineColumn > 0):
			mineBoard[mineRow + 1][mineColumn - 1] += 1
		if (mineColumn < (totalColumns - 1)):
			mineBoard[mineRow + 1][mineColumn + 1] += 1
	if (mineColumn > 0):
		mineBoard[mineRow][mineColumn - 1] += 1
	if (mineColumn < (totalColumns - 1)):
		mineBoard[mineRow][mineColumn + 1] += 1


for i in range(totalRows):
    mineBoard[i] = ['*' if x>99 else x for x in mineBoard[i]]

for i in range(totalRows):
    #Using the map function to call str for each element of mineBoard[i]
    #Creating a new list of strings and join into one string with str.join.
    #Then string formatting is used
   # print ('[%s]' % ', '.join(map(str, mineBoard[i])))
   print(' '.join(map(str, mineBoard[i])))



