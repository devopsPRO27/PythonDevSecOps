import math
import random

x = random.randint(0, 100)

print(type(x))


def hekef(r):
    return 2 * math.pi * r


print(hekef(12))


def add(x=0, y=0):
    return x + y


def sub(x=0, y=0):
    return x - y


def mul(x=0, y=0):
    return x * y


def div(x=0, y=1):
    return x // y

x=int(input("please enter a number :"))
y=int(input("please enter a number :"))
print(add(x,y))
print(mul(x,y))
print(sub(x,y))
print(div(x,y))



def get_in_range(max,min):
    while(True):
        x = int(input("please enter a number :"))
        if max >= x >= min:
            return x


print(get_in_range(100,10))