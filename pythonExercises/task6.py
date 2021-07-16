# 1 uppercase characters in string
string = 'This Is A String'
upperCase = [ch for ch in string if ch.isupper()]



# 2 zip two lists into a dictionary 
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

newDict = {student : subject for student, subject in zip(students, subjects)}
# newDict = dict(zip(students, subjects))



# 4 reverse a string using generator
def reverseGen(string):
    for i in range(len(string) - 1, -1, -1):
        yield string[i]

reverse = ''.join(reverseGen('Consultadd Training'))



# 5 decorator example
def decorator(func):
    def wrapper(*args, **kwargs):
        print('Inside wrapper')
        func(*args, **kwargs)
        print('Exiting wrapper')
    return wrapper

@decorator
def example(ex):
    print('{} function using decorator, adding args and kwargs handles any number of incoming parameters'.format(ex))

example('example')