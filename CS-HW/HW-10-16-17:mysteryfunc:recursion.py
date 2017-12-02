import sys

intValue  = int(input('Please enter an integer:\n'))


def sumdigits(intValue):
  if intValue == 0:
    return 0
  else:
    # do a integer division
    return (intValue%10) + sumdigits(intValue//10)



print(sumdigits(intValue))


