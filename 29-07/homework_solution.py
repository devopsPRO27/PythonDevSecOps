# numb1 = int(input('please enter a  number'))
# numb2 = int(input('please enter a  number'))
# numb3 = int(input('please enter a  number'))
#
# # if 200 > numb1 > 100:
#
# if (numb1 >= numb2) and (numb1 > numb3):
#     print(numb1)
# elif numb2 >= numb3:
#     print(numb2)
# else:
#     print(numb3)

#
# f = input("please enter a in this format n + n = n    n => number ")
# inputs = f.split()
# number1 = int(inputs[0])
# op = inputs[1]
# number2 = int(inputs[2])
# eq = inputs[3]
# ans = int(inputs[4])
# #
# # if number2+number1 == ans :
# #     print(True)
# # else:
# #     print(False)
#
#
# if op == '+':
#     print(number1 + number2 == ans)
# elif op == '-':
#     print(number1 - number2 == ans)
# elif op == '*':
#     print(number1 * number2 == ans)
# elif op == '/':
#     if number2 != 0:
#         print(number1 // number2 == ans)
# else:
#     print('invalid format')


# receive a number and print even or odd number

# x = int(input('please enter a number'))
#
# # if x % 2 == 0 :
# #     print('even')
# # else:
# #     print('odd')
#
# # answer = 'even' if x % 2 == 0 else 'odd'
# # print(answer)
#
# print('even') if x % 2 == 0 else print('odd')
#
#
# print(1) if x == 1 else print(2) if x == 2 else print('kol svar')

# x =  123 int    write a python code that write this specific
# number backward  321

x = int(input())
newx = 0
ahadot = 0

for i in range(1000):
    if x == 0:
        break
    ahadot = x % 10
    newx *= 10
    newx += ahadot
    x = x // 10
print(newx)

# ahadot = x % 10 # 3
# newx *=10  # 0
# newx += ahadot  #3
# x = x // 10  # 12
#
# ahadot = x % 10 # 2
# newx *=10  # 30
# newx += ahadot  #32
# x = x // 10  # 1
#
# ahadot = x % 10 # 1
# newx *=10  # 320
# newx += ahadot  #321
# x = x // 10  # 0


# receive number and print it 300 times

in1 = input()

print((in1 + '\n') * 300)

# for i in range(300):
#     print(in1)
