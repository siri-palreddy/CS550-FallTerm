# import the libraries you'll need
import tkinter
from tkinter import *
import time
from tkinter.messagebox import *
import sys
import random
from random import randint
import math
from PIL import ImageTk
from PIL import Image #This is the PIL Image library
#pip install pillow
from functools import partial

playerLevel = 2

if (playerLevel == 1):
    totalRows = 10
    totalColumns = 10
    mines = 10
if (playerLevel == 2):
    totalRows = 16
    totalColumns = 16
    mines = 40
if (playerLevel == 3):
    totalRows = 30
    totalColumns = 16
    mines = 99

def getRow(cellNumber):
    rowNumber = math.ceil(cellNumber/totalColumns)
    return rowNumber

def getColumn(cellNumber):
    columnNumber = cellNumber%totalColumns
    if (columnNumber == 0):
        columnNumber = totalColumns
    return columnNumber
    


mineBoard = [[0 for x in range(totalColumns)] for x in range(totalRows)]


totalCells = totalRows * totalColumns
randMines = list()
for i in range(mines):
    mineLocation = randint(0, totalCells)
    # To avoud duplicate mines
    while (mineLocation in randMines):
        mineLocation = randint(0, totalCells)      
    randMines.append(mineLocation)

for i in randMines:
    # As index start with zero we need to adjust the index
    iMineRow = getRow(i) - 1
    iMineColumn = getColumn(i) - 1
    #print(iMineRow)
    #print(iMineColumn)
    mineBoard[iMineRow][iMineColumn] = 100
    if (iMineRow > 0):
        mineBoard[iMineRow - 1][iMineColumn] += 1
        if (iMineColumn > 0):
            mineBoard[iMineRow - 1][iMineColumn - 1] += 1
        if (iMineColumn < (totalColumns - 1)):
            mineBoard[iMineRow - 1][iMineColumn + 1] += 1
    if (iMineRow < (totalRows - 1)):
        mineBoard[iMineRow + 1][iMineColumn] += 1
        if (iMineColumn > 0):
            mineBoard[iMineRow + 1][iMineColumn - 1] += 1
        if (iMineColumn < (totalColumns - 1)):
            mineBoard[iMineRow + 1][iMineColumn + 1] += 1
    if (iMineColumn > 0):
        mineBoard[iMineRow][iMineColumn - 1] += 1
    if (iMineColumn < (totalColumns - 1)):
        mineBoard[iMineRow][iMineColumn + 1] += 1

for i in range(totalRows):
    mineBoard[i] = ['*' if x>99 else x for x in mineBoard[i]]

print(mineBoard)
for i in range(totalRows):
    #Using the map function to call str for each element of mineBoard[i]
    #Creating a new list of strings and join into one string with str.join.
    #Then string formatting is used
    #print ('[%s]' % ', '.join(map(str, mineBoard[i])))
    print(' '.join(map(str, mineBoard[i])))
class Game:

    def __init__(self, master):
        self.mineFrame = Frame(master=master,bg='#00ff00',width=len(mineBoard)*50, height=len(mineBoard[i]*50))
        self.mineFrame.grid(row=1, columnspan=1)
        self.mineFrame.pack(side = LEFT, fill=BOTH)
        self.createButtons(self.mineFrame)
        
                
    def createButtons(self, master):
        self.mineBoardButtons = [[0 for x in range(totalColumns)] for x in range(totalRows)]
        self.image = ImageTk.PhotoImage(file="MN.png")
        for i in range(len(mineBoard)):
            for j in range(len(mineBoard[i])):
                #b = Button(master, bg='#818a2a', text=mineBoard[i][j],width=5,padx=0, pady=0)
                b = Button(master, bg='#818a2a',width=5,padx=0, pady=0,command=lambda iLocal = i,jLocal = j: self.buttonClick(iLocal,jLocal))
                #b = Button(master, bg='#818a2a',width=5,padx=0, pady=0,command=partial(buttonClick, i,j))
                #b.bind('Button-1',self.abc)
                b.grid(row=i,column=j)
                self.mineBoardButtons[i][j] = b
                #if (mineBoard[i][j] == '*'):
                 #   b.config(image=image,width="25",height="25")
                  #  b.image = image
                
        self.quitBtn = Button(self.mineFrame, text='Quit', command=self.quit)
        self.quitBtn.grid(row=i+1, columnspan=j+1)
        

    def abc(event):
        print ("clicked at", event.x, event.y)
        
    def quit(self):
        global root
        root.destroy()

    def buttonClick(self,m,k):
        #handle button click event
        btnVal = mineBoard[m][k]
        
        print(btnVal)    # do here whatever you want
        if (btnVal != '*'):
            if (btnVal == 0):
                btnTextVal = ""
            else:
                btnTextVal = btnVal
            self.mineBoardButtons[m][k].config(text=btnTextVal)
            self.mineBoardButtons[m][k].config(bg='grey')
            #self.mineBoardButtons[m][k].config(state='disabled')

        if (btnVal == '*'):
            self.mineBoardButtons[m][k].config(image=self.image,width="35",height="25")
            self.mineBoardButtons[m][k].config(bg='red')
            for i in range(len(mineBoard)):
                for j in range(len(mineBoard[i])):
                    if (mineBoard[i][j] == '*'):
                            self.mineBoardButtons[i][j].config(image=self.image,width="35",height="25")
            

def main():
    global root  # Needed to modify global copy of root
    root = Tk()
    root.title('Mine Sweeper')
    game = Game(root)
    root.mainloop() #mainloop is  an infinite loop that processes click events on minesweeper screen

# Execute the module as the main program
if __name__ == '__main__':
    main()
    
