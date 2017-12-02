import sys
import random

MAXHUNGERLEVEL = 50
MINHUNGERLEVEL = 20

class Dinosaur:
     def __init__(self, name, species, period, size,diet='Carnivorous',country='Unknown'): #must always put self first. 
#Class runs this def. name is optional, keep adding arguments after self
         self.name = name
         self.species = species
         self.diet = diet
         self.period = period # When it lived ; Ex: Late Cretaceous
         self.size = size # Meters
         self.country = country
         self.dnacode = 'ATCGGATTCGG'
         self.alive = False
         self.hungerLevel = 0

     def get_dynoreport(self):	#Showing main aspects of dino
         print("Name:",self.name)
         print("Species:",self.species)
         print("Diet:",self.diet)
         print("Period:",self.period)
         print("Size in Meters: ",self.size)
         print("Country: ",self.country)
         print('Hunger Level: ', self.hungerLevel)

     def comeAlive(self,clonedCode): #First make the extinct dinosaur come back to life
         if (clonedCode == self.dnacode):
             self.alive = True
             print("Your cloned DNA brought the dead dino back to earth.");
         else:
             print("Your cloned DNA did not match Dino DNA. Clone another frog! DNA code for ", self.name ,"is ", self.dnacode);

     def feed(self,foodType,amount): #The dinosaur is only a carnivore- eats cow and goat, hunger level depends on which animal is chosen
         if foodType.upper() == 'GOAT':
             if self.hungerLevel >= MAXHUNGERLEVEL:
                 print('I am full!')
                 return
             if amount>=0 and amount<10:
                 print('Yummy!')
                 self.hungerLevel += amount
             if amount<0:
                 print('Don\'t cheat me! Give me some food!')
             if amount >= 10:
                 print('I cannot eat in one sitting!')
             return
         if foodType.upper() == 'COW':
             if self.hungerLevel >= MAXHUNGERLEVEL:
                 print('I am full!')
                 return
             if amount>=0 and amount<5:
                 print('Yummy!')
                 self.hungerLevel += (2*amount)
             if amount<0:
                 print('Don\'t cheat me! Give me some food!') #If user enters negative number, dino responds
             if amount >= 5:
                 print('I cannot eat in one sitting!')
             return
         print('Feed me a cow or goat!') #If user tries to feed something else, dind can only eat cow/goat

     def run(self, distance): #Dino is running, after hungerLevel is too low, the dino wants to stop
         if self.hungerLevel <= MINHUNGERLEVEL: #I set minimum hunger level in global code
             print('I cannot run - Feed me')
             return
         if distance >0 and distance < 50:
             print('I like this!')
             self.hungerLevel -= 15
         if distance >= 50 and distance <100:
             print('I\'ll get tired soon...')
         return

     def noise(self):
         return print('I made a sound with dB value of ', #A function that randomly chooses a growling sound for the dino
random.randrange(50,101))

     def play(self, dinosaur): #The dino can play with other dinos- depends on the properties (period) of other dino
         if (self.period != dinosaur.period):
             print("I cannot play with you - you are not my type - u belong to %s period:" % dinosaur.period)
             return
         else:
             print("Thanks for the play date")
             return






Abelisaurus = Dinosaur("Abelisaurus","Comahuensis","Late Cretaceous",9,"Carnivorous","Argentina")
Melanorosaurus = Dinosaur("Melanorosaurus","Readi","Late Triassic",5,"Omnivorous","South Africa")
Syntarsus = Dinosaur("Syntarsus","Rhodesiensis","Late Triassic",2,"Carnivorous","Zimbabwe")

#Abelisaurus.get_dynoreport()
Abelisaurus.comeAlive('ATCGGATTCGG')
Abelisaurus.feed('goat', 25)
Abelisaurus.feed('goat', 9)
Abelisaurus.feed('goat', 9)
Abelisaurus.feed('goat', -3)
Abelisaurus.feed('cow', 4)
Abelisaurus.feed('goat', 9)
Abelisaurus.feed('goat', 9)
Abelisaurus.feed('goat', 9)
Abelisaurus.feed('goat', 9)
Abelisaurus.run(20)
Abelisaurus.run(25)
Abelisaurus.noise()
Abelisaurus.play(Melanorosaurus)
Melanorosaurus.play(Syntarsus)

