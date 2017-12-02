import sys
import random

#Properties:
#Amount of money, pin number
#Methods:
#Deposit, withdraw, open/close, interest, loans

class Bank:
	def __init__(self, userName, pin, accountNumber, moneyAmount = 0):
		self.userName = userName
        self.moneyAmount = moneyAmount
        self.pin = pin
        self.accountNumber = random.randrange(000000000, 100000000)



    def get_Bankreport(self):	#Showing main aspects of bank
     	print('The amount of money in your account is: ', self.moneyAmount)
     	print('Your pin number is: ', self.pin)
     	print('Your account number is: ', self.accountNumber)

    def open_Bank(self, pinNumber, pin):
        if pinNumber != self.pin:
        	print('Please try again! Hint, the pin number is 6785!')
        else:
        	print('Welcome to your bank account')
        return
	def deposit(self, moneyGive, moneyAmount):
 		if moneyGive <= 0:
  			print('Please deposit more than zero dollars.')
 		if moneyGive >= self.moneyAmount:
 			self.moneyAmount += moneyGive
  			print('Thank you for your deposition. You now have $', self.moneyAmount, ' in your account.')
  		return
  	def withDraw(self, moneyDraw, moneyAmount):
  		if moneyDraw > self.moneyAmount:
  			print('We apologize, but you must take out an amount less than or equal to ', moneyAmount, '.')
  		if moneyDraw<= self.moneyAmount:
  			self.moneyAmount -= moneyDraw
  			print('You have withdrawn $', moneyDraw, '. You now have $', self.moneyAmount, ' in your account.')
  		return
  	def interest(self, ):

  	def close_Bank(self)
  		a = input('Would you like to close your account?').upper()
  		if a == ('YES'):
  			print('Have a nice day!')
  			break
  		if a == ('NO'):
  			print('Continue your banking experience!')


     #def 

     #def feed(self,foodType,amount): #The dinosaur is only a carnivore- eats cow and goat, hunger level depends on which animal is chosen
       

     #def run(self, distance): 


     #def play(self, dinosaur): 
   

Siri.open_Bank()

