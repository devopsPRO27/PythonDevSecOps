# x = 3

# x.upper()

# print(10 / 0)


# 10 / 2 =  5
# 10 -2 -2 - 2 -2 -2 =0
#
# 10 -0 -0-0 ..... =00


# try:
#     y = int(input())
#     print(x / y)
# except:
#     print('please enter a positive number next time ')
# except ValueError :
#     print('please enter a number next time ')


# write a python code that reads from file1.txt in the
# same pwd
# this code should not fall or raise an exception if the file isn't exists

#
# try: # here we write the dangerous code
#     with open('file1.txt') as file:
#         print(file.read())
# except: # if exp raise we will catch it here
#     print('something went wrong')
# else: # no exp you can access this block
#     print("Done")
# finally: # finally keyword love every one and every
#     # situation so feel free to enter
#     print('always on the board')

# write a python program that receives
# from the user 2 numbers and divide
# them
# the code must handle all the exception
# and if we got a ZeroDivisionError we
# should ask the user to enter anew
# number
# if the code ended with no Errors
# print "hola totakhetooos"
# at the end write  "see you next
# time habibi"

def input_valid_number():
    while True:
        try:
            x= int(input('please enter a number :'))
            if x == 0:
                raise Exception('yo cant give me zero')
                # continue
        except ValueError:
            print('not valid input')
        else:
            return x


def div(x, y):
    try:
        return x/y
    except :
        print('you cant divide by zero')


in1 = input_valid_number()
in2 = input_valid_number()


print(div(in1,in2))


