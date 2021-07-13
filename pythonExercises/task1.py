#1 create three variables in a single line
a, b, c = 1, 2.01, 'string'



#2 create variable of type complex and swap with another integer type variable
varComp = 1 + 2j
print(type(varComp))    # prints <type 'complex'>
c, varComp = varComp, c
print(type(varComp))    # prints <type 'int'>



#3 swap two numbers with and without third variable
temp = b
b = a
a = temp
# or
a, b = b, a



#4 wap to take input and print in both python 2.x and 3.x
# python 2.x
userInput = (raw_input('Enter input : '))
print "Input from user: ", userInput
#python 3.x
userInput = str(input('Enter input : '))
print ("Input from user: ", userInput)



#5 wap to complete task
x, y = input("Enter two numbers between 1-10 : ").split()
z = int(x) + int(y)
result = 30 + z
print("Result = ", result)



#6 wap to check datatype
userInput = input("Enter input : ")
print('The data type of the input value is : {}'.format(type(userInput)))



#7 create variables using different naming formats
UpperCamelCase, lowerCamelCase, snake_case, UPPERCASE = 1, 2, 3, 4



#8 The value of the variable as well as the data type will change. Since python is an interpreted language, the last assigned value to the variable will be its new value and data type