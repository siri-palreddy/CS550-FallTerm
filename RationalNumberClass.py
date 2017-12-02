import sys
import random

class RationalNumber:
	def __init__(self, n, d):
		self.n = n #1/2
		self.d = d #1/3

	def __add__(self, other):
		n = self.n * other.d + self.d * other.n
		d = self.d * other.d
		return RationalNumber(n, d)
	def __sub__(self, other):
		n = self.n * other.d - self.d * other.n
		d = self.d * other.d
		return RationalNumber(n, d)
	def __mul__(self, other):
		n = self.n * other.d * self.d * other.n
		d = self.d * other.d
		return RationalNumber(n, d)
	def __truediv__(self, other):
		if (self.d * other.n) != 0:
			n = self.n * other.d *(1/(self.d * other.n))
			d = self.d * other.d
		return RationalNumber(n, d)

def main():
	a = RationalNumber(1,2)
	b = RationalNumber(1,3)
	print(a)
	print(b)
	print(a + b)
	print(a - b)
	print(a*b)
	print(a/b)

main()





	#def __mul__(self, n1, n2, n3):

	#def __add__(self, n1, n2, n3):

	#def __sub__(self, n1, n2, n3):

	#def __str__(self, n1, n2, n3):

	


#n3 = n1 + n2 #5/6
#n3 = n1 - n2 #1/6
#n3 = n1 * n2 #1/6
