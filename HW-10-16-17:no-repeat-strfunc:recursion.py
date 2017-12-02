import sys

strValue  = input("Please enter a string to clean up:\n")


def stringClean(strValue):
    # Takes care of empty string
    if not strValue:
        return ""
    if len(strValue) == 1:
        return strValue
    if strValue[0] == strValue[1]:
        return stringClean(strValue[1:]) #everything after 1 (:), inclusive
    return strValue[0] + stringClean(strValue[1:]) #All values will become [0], except last one, 
    												#as function goes through, then only goes 
    												#through the rest: the second one becomes 
    												#zero

#Case sensitive - Upper case and Lower case charcaters are treated as different
print(stringClean(strValue))

