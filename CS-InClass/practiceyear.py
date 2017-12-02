import sys

year = int(input("Pick a year!"))

year4 = year%4
year100 = year%100
year400 = year%400

x = bool(year4 == 0)
y = bool(year100 == 0)
z = bool(year400 == 0)

a = bool(z == y)

b = bool(x == a)

print(b)


