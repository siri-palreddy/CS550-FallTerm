
 #Class:
 #What we can keep track of
 #What we can do with the object

 #Card
 #Properties: Suit, Rank
 #Actions: None for one specific card

 #Dog:
 #Properties: Color (specify, but possible to randomize), Size (no need to specify), breed(specify), energy, name, hungry level, age, isAlive(should be true)
 #Actions: eat, bark, wag tail, roll over, fetch, sleep, run, walk, chase tail/squirrel

class Dog:
	def __init__(self, name, age, breed, color): #must always put self first. Class runs this def. name is optional, keep adding arguments after self
		self.color = color
		self.name = name
		self.age = age
		self.breed = breed
		self.size = 50#(meaning of number different. 50 could be pounds, or volume, or kg)
		self.energy = 50
		self.hunger = 50
		self.isAlive = True

	def eat(self, amount):
		if self.hunger > 0:
			print('Yummy!')
			self.hunger -= amount
			self.energy += amount*2
		else:
			print(self.name + ' isn\'t hungry')

	def stats(self):
		print('Name: ' + self.name)
		print('Energy: ' + str(self.energy))
		print('Hunger: ' + str(self.hunger))




mydog = Dog('Tim', 5, 'Retriever', 'Brown')
mydog.stats()
mydog.eat(5)
mydog.eat(7)
mydog.eat(35)
mydog.stats()
mydog.eat(100)
mydog.eat(100)
mydog.stats()



