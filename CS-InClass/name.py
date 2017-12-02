import sys

print('Hello, ', end= ' ')
print(sys.argv[1], end= '')
print('! Welcome.')
username = input('What is your full name?')
age = int(input('Please enter your age:'))
birthday = str(input('When is your birthday?'))
color = input('What is your favorite color?')
print ('That color, ' + color + ', is my favorite color too!')
number = int(input('What\'s your favorite number?'))
print(number + 5)
import sys

x = str('It\'s a lovely day, isn\'t it, ')
print(x + username + '.')
