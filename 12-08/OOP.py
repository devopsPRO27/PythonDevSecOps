# x = int()
# y = str()
# z = float()
# a = list()
# b = dict()
# c = tuple()
# g = bool()
# h = set()
#
#
# print(x)
# print(y)
# print(z)
# print(a)
#
#
# kobis_dog_age=15
# kobis_dog_name='gibor'
# kobis_dog_kind='poodle'
#
# Dog


# class Dog:
#     #DATA
#
#     #func
#     def bark(self):
#         print('whoooph whoooph ')
#     def eat(self ,food):
#         print(f'eating ..... {food}')
#
# class Cat:
#     def mewoing(self):
#         print('meeaaaaoo')
#
#
# chewawa = Dog()
# hertzel = Cat()
# print(type(chewawa))
# print(isinstance(chewawa,Dog))
# print(chewawa)
# chewawa.bark()
# chewawa.eat('apple')
# hertzel.mewoing()

# class Phone:
#     def turn_on(self):
#         print('turning on ....')
#
#     def turn_off(self):
#         print('turning off ....')
#
#     def dial(self, phone_number):
#         # if len(phone_number) >= 9:
#         #     return True
#         # return False
#         return len(phone_number) >= 9
#
#
# iphone = Phone()
#
# choice = int(input('press 1 to turn on the phone 2 to turn off 3 to dail '))
# actions = {1: 'turn On', 2: 'turn off', 3: 'dial'}
#
# if actions[choice] == 'turn On':
#     iphone.turn_on()
# if actions[choice] == 'turn off':
#     iphone.turn_off()
# if actions[choice] == 'dial':
#     print(iphone.dial('0526618010'))


class Cat:
    # DATA
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def print_name(self):
        print(f'{self.name}')
    def __repr__(self):
        return f'repr name ={self.name} age ={self.age}'
    def __str__(self):
        return f'name ={self.name} age ={self.age}'


# c1= Cat()
#
# c1.name = 'hatool'
# c1.age =19
#
# c2= Cat()
# c2.color='red'

c3 = Cat('hatool', 19, 'red')
c4 = Cat('jojo', 24, 'white')

c4.print_name()
c4.name = 'timon'
c4.print_name()
print(c4)
print(c3)