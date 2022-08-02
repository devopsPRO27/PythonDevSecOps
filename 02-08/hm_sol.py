# 1

# write a pyhton code that recive from the user a
# number and sum the digits of this number and then
# \print the answer
#
# number = int(input('please enter a number'))
# sum = 0
#
# for i in range (1000):
#     if number == 0:
#         break
#     ahadot = number % 10
#     number = number // 10
#     sum += ahadot  # sum = sum + ahadot
#
# print(sum)


# 2
# username = input('please enter you name')
#
# username = username.lower()
# username_length = len(username)
# new_name=''
#
# for i in range(username_length):
#     if username[i] == ' ':
#         break
#     if username[i] in ['a', 'b', 'c', 'o']:
#        new_name += username[i].upper()
#     else:
#         new_name+=username[i]
#
#
#
# print(new_name)

sum = 0
for i in range(7):
    sum += int(input('please enter a number :'))
print(sum / 7)
