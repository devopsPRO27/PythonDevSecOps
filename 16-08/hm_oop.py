# def args1(*args):
#     print(type(args))
#
#
# def kwargs(**kwargs):
#     print(kwargs)
#
#
# args1(2,333,415,1516,'sun')
# kwargs(name = 'ori', age= 19)
#
# t1 = (12, 444, 151, 'joey doesn\'t share food')
#
# class AnimalAndFish:
#     def __init__(self):
#         print('another animal on the way')
#     def foo(self):
#         print('fooo')
#
#
# ant = AnimalAndFish()
# ant1 = AnimalAndFish()
# ant2 = AnimalAndFish()
#
# ant.foo() # method
# 'st'.upper() # ,method
# [].append() #method
#
# len([2,2])  # funcion

# def sorted_numbers(*args):
#     return sorted(list(args))
#
#
# print(sorted_numbers(4, 2, 11, 7, 7, 1, -7))
#
#
# def comp_kwargs_dict(dict1, **kwargs):
#     # for k1,v1 in dict1.items():
#     #     for k2,v2 in kwargs.items():
#     #         if k1 != k2 or v1 != v2:
#     #             return False
#     #
#     return dict1 == kwargs
#
#
# print(comp_kwargs_dict({'name': 2, 'value': 7}, value=3, name=2))

class Superhero:
    def __init__(self,crush):
        print('new super hero is born')
        self.crush = crush

    def fly(self):
        print('0-100 really quik')

    def climb(self):
        print('climbing ....')

    def force_speed(self):
        print('Run run ......')
    def __str__(self):
        return f'superhero {self.crush}'
    def __repr__(self):
        return f'superhero {self.crush}'



hulk = Superhero('catwoman')
magin_boo = Superhero('vagita')
superman = Superhero('louis')
print(hulk.crush)
del hulk.crush
# print(hulk.crush)

hulk.fly()
magin_boo.climb()
superman.force_speed()

print(magin_boo)