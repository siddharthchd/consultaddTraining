# 1 calculate formula 
import math

def formula(inp):
    C = 30
    H = 50
    num = ''.join(inp.split(','))
    print(math.sqrt((2 * C * int(num)) / H))

userInput = input('Enter comma separated sequence : ')
formula(userInput)



# 2 shape and square class
class Shape:
    a = 0
    def area(self):
        return self.a 

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2



# 3 
class ThreeSum:
    
    def threeSum(self, nums):
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[left] + nums[i] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

sum3 = ThreeSum()
threeSumList = sum3.threeSum([-25, -10, -7, -3, 2, 4, 8, 10])



# 4 class time 
class Time:
    
    def __init__(self, hours, minutes):
        self.hours  = hours
        self.minutes = minutes
    
    def addTime(self, t2):
        sumHours = t1.hours + t2.hours
        sumMins = t1.minutes + t2.minutes
        if sumMins >= 60:
            if sumMins % 60 > 0:
                sumHours += 1
                sumMins = sumMins % 60
            else:
                sumHours += 1
                sumMins = 0

        return sumHours, sumMins

    def displayTime(self, hours, minutes):
        print('Time : {} hr {} mins'.format(hours, minutes))

    def displayMinutes(self, hours, minutes):
        totalMins = (hours  * 60) + minutes
        print('Time in minutes : {} mins'.format(totalMins))

t1 = Time(1, 30)
t2 = Time(2, 30)
thrs, tmins = t1.addTime(t2)
t1.displayTime(thrs, tmins)



# 5 person class
class Person:
    age = 1
    
    def __init__(self, age):
        if not age < 0:
            self.age = age
        else:
            self.age = 0
            print('Age is not valid, setting age to 0.')

    def yearPasses(self, raiseBy):
        self.age += raiseBy
        print('You are now {} years old'.format(self.age))
    
    def amIOld(self):
        if self.age < 13:
            print('You are young')
        elif self.age >= 13 and self.age <= 19:
            print('You are a teenager')
        else:
            print('You are old')

p1 = Person(-1)
p2 = Person(4)
p3 = Person(15)
p4 = Person(38)
p2.amIOld()
p3.amIOld()
p4.amIOld()
p4.yearPasses(4)