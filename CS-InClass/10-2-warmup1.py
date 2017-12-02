import sys

def avg(a,b = 0,c = 0):
	try:
		#a1 = int(a)
		#b1 = int(b)
		#c1 = int(c)
		d = ((int(a) + int(b) + int(c))/3)
		return d
	except (TypeError):
		print('The values cannot be averaged.')
		return None



print(avg(input('Num1: '), input('Num2: '), input('Num3: ')))
#print(avg(5))
#print(avg(5,4))
#print(avg(5,4,3))
#print(avg('5','6','7'))
#sub(7,6)
#sub('7','6')
#sub('a','b')