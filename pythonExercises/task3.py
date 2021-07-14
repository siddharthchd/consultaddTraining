# 1 list of elements with different data types
dTypeList = [1, 2, 'a', 'b', 'c', 1 + 2j, 2 + 3j, 1.2, 2.3, 3.4]



# 2 slicing
x = [1, 2, 3, 4, 5]
print(x[2:])    # will print [3, 4, 5]



# 3 sum and product of items in list
from functools import reduce    

def sumMult(x):
    sum = reduce(lambda a, b : a + b, x)
    prod = reduce(lambda a, b : a * b, x)

    return sum, prod



# 4 largest and smallest in list
def largestSmallest(x):
    return max(x), min(x)



# 5 remove even from list
def removeEven(x):

    newList = [a for a in x if a%2 != 0]
    return newList



# 6 square of first and last five
squaredList = [x ** 2 for x in range(1, 31) if x <= 5 or x > 25]



# 7 replace element with list
def replaceEle(x, y):
    return x[:-1] + y



# 8 concatenate dictionaries
def dictConcat(x, y):
    x.update(y)
    return x



# 9 dictionary with x:x*x
def squaredDict(n):
    sdict = {}
    for x in range(1, n + 1):
        sdict[x] = x ** 2
    return sdict



# 10 convert to list and tuple
def returnString():
    inputString = input('Enter comma separated numbers : ')
    stringList = inputString.split(', ')
    stringTuple = tuple(stringList)
    return stringList, stringTuple