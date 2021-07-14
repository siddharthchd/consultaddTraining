# 1 reverse a string
def reverseString(x):
    return x[::-1]



# 2 upper and lower case letters in string
def countUpperLower(x):
    if type(x) != str:
        print('Should be a string')
    count = {'lower' : 0, 'upper': 0}
    
    for ch in x:
        if ch.islower():
            count['lower'] += 1
        elif ch.isupper():
            count['upper'] += 1


    print('No. of Uppercase characters : {} No. of Lowercase characters : {}'.format(count['upper'], count['lower']))



# 3 return unique elements from first list
def returnUnique(x):
    return set(x)



# 4 sort hyphen separated sequence of words
def hyphenSeq(x):
    # assuming x is a hyphen separated seq
    x = sorted(x.split('-'))
    return ('-').join(x)



# 5 capitalize string 
def returnUpper(x):
    return x.upper()



# 6 return sum of numbers present in string format
def returnSum(a, b):
    print(int(a) + int(b))



# 7 check length of strings
def checkLen(string1, string2):

    if len(string1) == len(string2):
        print('{}\n{}'.format(string1, string2))
    elif len(string1) > len(string2):
        print(string1)
    else:
        print(string2)



# 8 tuple of squares
def tupleSquares():
    tsq = tuple(i ** 2 for i in range(1, 21))
    print(tsq)



# 9 showNumbers functions
def showNumbers(limit):
    result = {}
    for i in range(limit + 1):
        if i % 2 == 0:
            result[i] = 'EVEN'
        else:
            result[i] = 'ODD'

    print(result)



# 10 filter list
def filterList():
    x = [i for i in range(1, 21)]
    x = filter(lambda x: x % 2 == 0, x)
    return(list(x))



# 11 use map and filter
def squareOfEven(x):
    x = list(filter(lambda x: x % 2 == 0, x))
    x = list(map(lambda x: x ** 2, x))
    return x

print(squareOfEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



# 12 try except 
def divideByZero():
    try:
        print(5 / 0)
    except ZeroDivisionError:
        print("Can't divide by zero")



# 13 flatten list
def flattenList(x):
    s = ''.join(map(str, x))
    return int(s)



# 14 not divisible by 5 but multiple of 7
from functools import reduce

def threeNotSeven(x):
    x = list(filter(lambda a: a%3 != 0, x))
    x = list(filter(lambda a: a%7 == 0, x))
    return x



# 15 traditional and map
def traditional(x):
    return x*x

print(list(map(traditional, [1, 2, 3, 4, 5])))



# 16
# (i)   -> 2
# (ii)  -> after f
#       -> after f?