import sys

m = int(input('Please enter a month (1-12): '))
d = int(input('Please enter a day (1-31): '))
y = int(input('Please enter a year: '))


y0 = y - int((14 - m) /12)
x = y0 + int(y0/4) - int(y0/100) + int(y0/400)
m0 = m + 12 * int((14 - m) / 12) - 2
d0 = (d + x + int((31 * m0) / 12)) % 7

numbers_to_daysx = {
         0: "Sunday",
         1: "Monday",
         2: "Tuesday",
         3: "Wednesday",
         4: "Thursday",
         5: "Friday",
         6: "Saturday"
}
print(numbers_to_daysx[d0])
