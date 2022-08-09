# def greet(name):
#     message='b'
#
# print(message)


# message = 'a'
#
# def greet1():
#     message = 'b'
#     print(message)
#
# print('main   '+message)
# greet1()


# x = 2
#
#
# def foo():
#     global x
#     x = 13
#     print(x)
#
#
# foo()
# print(f'main  {x}')

avg =0

def multi_avg(*arg):
    global avg
    multi = 1
    for i in arg:
        multi*=i
    avg = multi / len(arg)
    return multi

m = multi_avg(5,44,66,24)

print(m)
print(avg)
