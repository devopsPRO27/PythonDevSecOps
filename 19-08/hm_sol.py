# import json
#
# class Josh:
#     def __init__(self, tattoos):
#         self.__tattoos = tattoos
#
#     @property
#     def tattoos(self):
#         return self.__tattoos
#
#     @tattoos.setter
#     def tattoos(self, new_tattoos):
#         if len(new_tattoos) > 8:
#             self.__tattoos = new_tattoos
#
#     def eat(self):
#         '''this func prints josh fav food
#         :param none
#         :return void'''
#         print('330 md ')
#
#
# j1 = Josh('DEAD woman')
# j2 = Josh('DEAD woman')
# j1.tattoos = 'BATMAN'
# print(j1.tattoos)
# print(j1)
# print(j2)
#
# print(help(Josh))
# print(dir(Josh))
#
import math


# class Shape:
#     def __init__(self, name, perimeter, area):
#         self.__name = name
#         self.__perimeter = perimeter
#         self.__area = area
#
#     @property
#     def area(self):
#         return self.__area
#     @area.setter
#     def area(self, new_area):
#         self.__area = new_area
#     @property
#     def perimeter(self):
#         return self.__area
#
#     @perimeter.setter
#     def perimeter(self, new_perimeter):
#         self.__area = new_perimeter
#
#     def __eq__(self, other):
#         q1 = (self.area + self.perimeter) / 2
#         q2 = (other.area + other.perimeter) / 2
#
#         return  q1 == q2
#
#     def __gt__(self, other):
#         return self.area > other.area
#
#     def __ge__(self, other):
#         return self.area >= other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __str__(self):
#         return f'this Shape name is = {self.__name}'
#
#
# triangle = Shape('toto', 12, 10)
#
# circle = Shape('coco', 12, 13)
# print(triangle)
#
# print(triangle == circle)
# print(circle > triangle)
# print(circle < triangle)
# print(circle <= triangle)
# print(circle <= triangle)

class Angle:
    def __init__(self,**kwargs):
        self.__dict__=kwargs

    @property
    def degree(self):
        return self.__degree


# a1 = Angle(90, 'zodiak')
# print(a1.__dict__)
# a1.__dict__['_Angle__degree'] = 'urii'
# print(a1.degree)
# print(a1.__dict__)

uri = {'name': 'uri', 'age': 18, 'car': 'mustang'}
a2 = Angle(name = 'edo',car = 'bmw z4')
print(a2.car)
