import sys


s = int(input('Please enter the speed: '))
bday = input('Please enter your birthday date. Enter it as a month.day. Example: Today is September 25, so I would enter 9.25: ')
date = input('Please enter today\'s date, without the year. Enter it as a month.day. Example: Today is September 25, so I would enter 9.25: ')

if bday != date:
	if s <= 60:
		print('No ticket!')
	elif 60 < s and s < 80:
		print('Small ticket')
	else:
		print('Big ticket')
else:
	if bday == date and s <= 65:
		print('No ticket! And Happy Birthday')
	elif 65 < s < 85:
		print('Small ticket!. Happy B-Day!')
	else:
		print('Big ticket. Happy B-Day!')
