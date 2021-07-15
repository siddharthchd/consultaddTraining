# 1 syntax error
try:
    eval('x === x')
except SyntaxError:
    print("Syntax error")



# 2 argv
from sys import argv

program, fileName = argv
while True:
    try:
        file = open(fileName)
        fileContent = file.read()
        print(fileContent)
        file.close()
        break
    except:
        fileName = input('No such file. Enter correct name :.. ')
        continue



# 3 number exactly four digits
num = int(input('Enter a number: '))
while True:
    try:
        if num < 1000 or num > 9999:
            raise ValueError
        else:
            break
    except ValueError:
        num = int(input('Please enter a 4 digits number: '))
        continue



# 4 login attempts
attempts = 0
while attempts < 3:
    userName = input('Enter username : ')
    password = input('Enter password : ')
    rePassword = input('Re-Enter password : ')
    if rePassword != password:
        print('incorrect')
        attempts += 1
        if attempts == 3:
            print('Too many failed attempts')
    else:
        print('nice')
        break



# 6 file handling even length strings only
try:
    with open('doc.txt') as file:
        content = file.read()

    words = content.split()
    evenWords = []
    for word in words:
        if len(word) % 2 == 0:
            evenWords.append(word)
    print(evenWords)


except:
    print('Error')