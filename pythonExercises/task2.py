# 1
def divisibleBy3(num):
    if (num % 3 == 0) and (num % 5 == 0):
        print("Consultadd - Python Training")
    elif (num % 3 == 0):
        print("Consultadd")
    elif (num % 5 == 0):
        print("Python Training")

#divisibleBy3(15)



# 2
def performChoice():

    print('Enter 1 for Addition')
    print('Enter 2 for Subtraction')
    print('Enter 3 for Division')
    print('Enter 4 for Multiplication')
    print('Enter 5 for Average')

    choice = int(input('Enter your choice : '))
    result = 0

    while choice > 0:
        num1, num2 = (input('Enter two numbers : ').split())
        num1, num2 = int(num1), int(num2)
        if choice == 1:
            result = num1 + num2
            break
        elif choice == 2:
            result = abs(num1 - num2)
            break
        elif choice == 3:
            if num2 != 0:
                result = num1 / num2
            else: 
                print('Cant divide by zero')    
            break
        elif choice == 4:
            result = num1 * num2
            break
        elif choice == 5:
            num3, num4 = input('Enter two more numbers : ').split()
            num3, num4 = int(num3), int(num4)
            result = (num1 + num2 + num3 + num4) / 4
            break
        else:
            print("Invalid Choice")
            break

    if result < 0: print("NEGATIVE")
    print('Result : ', result)

#performChoice()



# 3 Flowchart
def flowchart():
    a, b, c = 10, 20, 30
    avg = (a + b + c) / 3
    print("avg = ", avg)

    if (avg > a and avg > b and avg > c):
        print("avg is higher than a, b, c")
    elif (avg > a and avg > b):
        print("avg is higher than a, b")
    elif (avg > a and avg > c):
        print("avg is higher than a, c")
    elif (avg > b and avg > c):
        print("avg is higher than b, c")
    elif (avg > a):
        print("avg is just higher than a")
    elif (avg > b):
        print("avg is just higher than b")
    elif (avg > c):
        print("avg is just higher than c")
    else:
        print("do nothing")

#flowchart()



# 4 break
while(True):
    num = int(input('Enter integer : '))
    if num < 0:
        print("It's Over")
        break
    else:
        print('Good Going')



# 5 Divisible by 7 but not a multiple of 5
result = []
for num in range(2000, 3201):
    if num % 7 != 0:
        continue
    else:
        if num % 5 != 0:
            result.append(num)
print(result)



# 6 output of code

# -> 123

# -> 0
#    error
#    1
#    error
#    2

# -> 0
#    1
#    2
#    3
#    4



# 7 - 0 to 6 except 3 and 6
for num in range(0, 7):
    if num == 3 or num == 6:
        continue    
    print(num)
        


# 8 count number of letters and numbers
def countChar():
    inputString = input('Enter alphanumeric value : ')
    count = {'letters' : 0, 'numbers' : 0}
    for char in inputString:
        if char.isalpha():
            count['letters'] += 1
        elif char.isnumeric():
            count['numbers'] += 1

    print('Letters {}   Digits {}'.format(count['letters'], count['numbers']))

#countChar()



# 9 
import random

luckyNumber = random.randint(1, 10)

def guessLuckyNumber():
    number = 0
    answer = ''

    while(answer != 'no'):
        number = int(input('Guess the Lucky number between 1-10 : '))
        if number == luckyNumber:
            print("Correct guess")
            break
        else:
            answer = input('Hard Luck. Do you want to guess again?')

#guessLuckyNumber()



# 10

number = random.randint(1, 10)

def askFive():
    counter = 1
    
    while counter <= 5:
        guess = int(input('Enter in the {} number : '.format(counter)))
        if guess == number:
            print('Good guess!')
        else:
            print('Try Again')
        counter += 1

    print('Game over!')

#askFive()



# 11 add break to above program
def askFive():
    counter = 1
    
    while counter <= 5:
        guess = int(input('Enter in the {} number : '.format(counter)))
        if guess == number:
            print('Good guess!')
            break
        else:
            print('Try Again')
        counter += 1

    if guess != number: print("Sorry but that was not very successful")
    print('Game over!')

#askFive()