# import the libraries you'll need
import tkinter
from tkinter import *
import time
from tkinter.messagebox import *
import sys
import random
from random import randint
import math
#pip install pillow
from functools import partial
import math

playerLevel = 1

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

mineCounter = mines

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
        self.image = PhotoImage(file="MN.png")
        self.lostImage = PhotoImage(file="LOST.png")
        self.wonImage = PhotoImage(file="WIN.png")
        self.normalImage = PhotoImage(file="NORMAL.png")
        self.createButtons(self.mineFrame)
        

                
    def createButtons(self, master):
        self.mineBoardButtons = [[0 for x in range(totalColumns)] for x in range(totalRows)]
        for i in range(len(mineBoard)):
            for j in range(len(mineBoard[i])):
                b = Button(master, bg='#818a2a',width=5, padx=0, pady=0,command=lambda iLocal = i,jLocal = j: self.buttonClick(iLocal,jLocal))
                b.bind("<Button-3>", lambda event,iLocal = i,jLocal = j: self.rightClick(event,iLocal,jLocal))
                b.grid(row=i,column=j)
                self.mineBoardButtons[i][j] = b
                
        centerCol =   math.ceil(totalColumns/2)      
        self.quitBtn = Button(self.mineFrame, text='Quit', width=5,command=self.quit)
        self.quitBtn.grid(row=i+1, column=centerCol-1)

        self.countBtn = Button(self.mineFrame, text=mineCounter, width=5)
        self.countBtn.grid(row=i+1, column=centerCol+1)

        self.statusBtn = Button(self.mineFrame, text='', width=5, padx=0, pady=0,command=lambda : self.lost())
        self.statusBtn.grid(row=i+1, column=centerCol+3)
        self.statusBtn.config(image=self.normalImage,width="25",height="25")  

    def rightClick(self,event,m, k):
        # Use gloabl counter and not initiate a local variable called mineCounter
        global mineCounter
        btnVal = mineBoard[m][k]
        #If this is a mine then disable the mine
        if (btnVal == '*'):
            self.mineBoardButtons[m][k].config(highlightbackground='blue')
            self.mineBoardButtons[m][k].config(state='disabled', relief=SUNKEN)
            mineCounter -=1
            self.countBtn.config(text=mineCounter)

        if (mineCounter == 0):
            #Game is won as all mines are detected
            self.statusBtn.config(image=self.wonImage,width="25",height="25")  
        
    def quit(self):
        self.root.destroy()
        sys.exit()

    def buttonMineCountClick(self, mineCounter):
        self.countBtn.config(text=mineCounter)

    def buttonClick(self, m, k):
        #handle button click event
        btnVal = mineBoard[m][k]
        
        if (btnVal != '*'):
            if (btnVal == 0):
                btnTextVal = ""
                self.selectSafeButtons(m,k)
            else:
                btnTextVal = btnVal
            self.mineBoardButtons[m][k].config(text=btnTextVal)
            self.mineBoardButtons[m][k].config(highlightbackground='grey')
            #self.mineBoardButtons[m][k].config(state='disabled')

        if (btnVal == '*'):
            # Clicked on a mine - Show all mines and quit
            self.mineBoardButtons[m][k].config(image=self.image,width="25",height="25")
            #self.mineBoardButtons[m][k].config(image=self.image)
            self.mineBoardButtons[m][k].config(highlightbackground='red')
            for i in range(len(mineBoard)):
                for j in range(len(mineBoard[i])):
                    if (mineBoard[i][j] == '*'):
                        #self.mineBoardButtons[i][j].config(image=self.image,width="25",height="25")
                        self.mineBoardButtons[i][j].config(image=self.image,width="25",height="25")
                        self.statusBtn.config(image=self.lostImage,width="25",height="25")


    def selectSafeButtons(self, m, k):
        if (m > 0):
            self.setButtonText(m-1, k)
            if (k>0):
                self.setButtonText(m-1, k-1)
            if(k< (totalColumns-1)):
                self.setButtonText(m-1, k+1)
        if (m < (totalRows-1)):
            self.setButtonText(m+1, k)
            if (k>0):
                self.setButtonText(m+1, k-1)
            if(k<(totalColumns-1)):
                self.setButtonText(m+1, k+1)
        if (k>0):
            self.setButtonText(m, k-1)
        if(k< (totalColumns-1)):
            self.setButtonText(m, k+1)
            
    def setButtonText(self, m, k):
        BGCOLOR = 'grey'
        btnVal = mineBoard[m][k]
        if btnVal != 0:
            self.mineBoardButtons[m][k].config(text=btnVal)
        self.mineBoardButtons[m][k].config(bg=BGCOLOR)

    def lost(self):
        time.sleep(1.5)
        msg = 'You lost the game! Do you want to play again?'
        result = askquestion('Play again?',msg)
        
        if result == 'yes' or result == 'Yes':
            self.reset()
        else:
            self.quit()

    def quit(self):
        global root
        root.destroy()

    def reset(self):
        mineCounter = mines
        self.countBtn.config(text=mineCounter)
        self.statusBtn.config(image=self.normalImage,width=25,height=25)  
        
        for i in range(len(mineBoard)):
            for j in range(len(mineBoard[i])):
                b = self.mineBoardButtons[i][j]
                if (mineBoard[i][j] == '*'):
                    #b.config(bg='#818a2a', text='')
                    #b.config(state='normal', relief=RAISED)
                    #b.config(image='',width=5, padx=0, pady=0)
                    b.destroy()
                    b = Button(self.mineFrame, bg='#818a2a',width=5, padx=0, pady=0,command=lambda iLocal = i,jLocal = j: self.buttonClick(iLocal,jLocal))
                    b.bind("<Button-3>", lambda event,iLocal = i,jLocal = j: self.rightClick(event,iLocal,jLocal))
                    b.grid(row=i,column=j)
                    self.mineBoardButtons[i][j] = b
                else:
                    b.config(bg='#818a2a', text='')
                    b.config(state='normal', relief=RAISED)
        
def main():
    global root  # Needed to modify global copy of root
    root = Tk()
    root.title('Mine Sweeper')
    game = Game(root)

    root.mainloop() #mainloop is  an infinite loop that processes click events on minesweeper screen

# Execute the module as the main program
if __name__ == '__main__':
    main()

