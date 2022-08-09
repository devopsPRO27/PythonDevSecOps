# lis = [1,2,3,4,5]
# lis2 = list(range(15))
# lis3 = lis+lis2
# lis4 = [['x','e'],['s','o']]
# lis5 = [2,'hodi',True,5.5]
# lis6 = [0,1] * 5
# lis7 = list('piz za')
#
# lis8 = list('hotdog is life')
# print(lis[0:2])
# print(lis2)
# print(lis3)
# print(lis4)
# print(lis5)
# print(lis6)
# print(lis7)
# print(lis8)

numbers = [1, 2,3,4,5,6,7,8,9]

first, second , *third = numbers

first1, *between , last = numbers

# print(first)
# print(second)
# print(third)
print(first1)
print(between)
print(last)
