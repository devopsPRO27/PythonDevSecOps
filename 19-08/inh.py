# Don't repeat yourself

# class Animal:  # super class
#     def eat(self):
#         print('eating')
#     def make_Sound(self):
#         print('ooooooo')
#     def __str__(self):
#         return f'Animal class str'
#
#
# class Dog(Animal):  # subclass
#     def make_Sound(self):
#         print('wroooph wrooooph')
#     def __str__(self):
#         return 'Dog class'
#
#
# class Cat(Animal):
#     def jump(self):
#         print('jumping ...')
#
#
# d1 = Dog()
# d1.eat()
# d1.make_Sound()
# print(d1)
#
# c1 = Cat()
# c1.eat()

class Shape:
    def __init__(self, area, hekef):
        self.area = area
        self.hekef = hekef

    def clac_hekef(self):
        pass

    def calc_are(self):
        pass


# class Triangle(Shape):
#     def __init__(self,area,hekef, a, b, c, h):
#         Shape.__init__(self,area,hekef)
#         self.a = a
#         self.b = b
#         self.c = c
#         self.h = h
#
# class Circle(Shape):
#     def __init__(self,hekef,area,r):
#         Shape.__init__(self,area,hekef)
#         self.r=r
#
#
# t1 = Triangle(13,22,3, 5, 3, 6)
# print(t1.area)
#
# c1= Circle(224,21,4)
# print(c1.hekef)


class Food:
    def get_cal(self):
        return 0


class Pizza(Food):

    def get_cal(self):
        return 1800


class Shawarma(Food):
    def get_cal(self):
        return 3600


def print_cal(foods):
    for food in foods:
        print(food.get_cal())


marg = Pizza()
lafa = Shawarma()
pita = Shawarma()

f=[marg,lafa,pita]
print_cal(f)
