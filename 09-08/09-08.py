# def avg():
#     print(95)
#
# def get_avg():
#     return 'hii'
#
# avg()
#
# x = print('2')
#
# a=get_avg()
# b=get_avg()
#
# print(a+b)

# def greet(firstname = None , lastname = '' ):
#     print(f'hello sir , good morning {firstname} {lastname}')
#
#
# greet('ron' , 'yanai' )
# greet('kobi','nana')
#
# greet('yuval')
# greet(lastname='zoubi')
# greet(firstname='amit',lastname='yawza')
# greet(lastname='yawza',firstname='amit')
# greet()


# def power(x ,y ):
#     return x**y
#
# ans = power(2,2)
#
# print(ans)
#
# r = round(5.2)
# print(r)
#
# name_len=len('alon')
# print(name_len)


# def hello_with_name(name):
#     print(name)
#
# hello_with_name('ella')
#

# write a python function that receives 3 numbers x,y,z and return the greatest number
# if the user sends 2 numbers define the 3 rd  0
# etgar  if the 3 number wasn't defined  do not return it even if its the greatest

# def max(x, y, z='0'):
#     if z != '0':
#         if x > y and x > z:
#             return x
#         elif y > z:
#             return y
#         else:
#             return z
#     else:
#         return x if x > y else y
#         # if x > y:
#         #   return x
#         # else:
#         #   return y
#
#
# print(max(2, 5, 8))
# print(max(2, 5))
# print(max(-2, -5))
# print(max(-2, -5, 0))
# print(max(-5, -2))


def my_max(*args):
    print(args)
    print(type(args))
    # big = args[0]
    # for i in args:
    #     if big < i:
    #         big = i
    # return big
    print(sorted(args,reverse=True))
    return sorted(args)[-1]



big=my_max(1, 2, 35, -55, 22, 11)
print(big)
