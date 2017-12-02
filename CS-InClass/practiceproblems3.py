import sys

import random

a = random.random()
b = random.random()
c = random.random()
d = random.random()
e = random.random()

x = (a + b + c + d + e)/5

print('This was a: ', a)
print('This was b: ', b)
print('This was c: ', c)
print('This was d: ', d)
print('This was e: ', e)

print('This is the average of the values: ', x)
print('This is the maximum value: ', max(a, b, c, d, e))
print('This is the minimum value: ', min(a, b, c, d, e))