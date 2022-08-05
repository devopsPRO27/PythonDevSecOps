# 2

# for i in range(0, 100, 5):  ## הגדרת קפיצות
#     print(i)
#
# for i in range(1000, 100, -23):  ## טווח בסדר יורד
#     print(i)

# 3
# numbers = []
# for i in range(5, 15):
#     numbers.append(i)
# print(numbers)

# number = int('hodi')
# numbers_merged = list(range(1, 7)) + list(range(3)) # merge
# numbers_append = list(range(1, 7))
# numbers_append.append(list(range(3)))
#
# numbers_merged += list(range(19))
#
#
# print(numbers_merged)
# print(numbers_append)

# lists

# board = [['x','o','-'],
#          ['o','x','-'],
#          ['o','o','x']]
#
# line3= board[2]
#
#
# print(line3[1])
# print(board[2][1])
#

board2 = [['x', 'x', 'x'],
          ['o', 'x', '-'],
          ['o', 'x', 'o']]



y=1
if (board2[y][y] == board2[y-1][y-1] == board2[y+1][y+1] and board2[y][y] != '-') \
        or (board2[y][y] == board2[y-1][y +1] == board2[y + 1][y - 1] and board2[y][y] != '-'):
    print('win')
else:
    for x in range(3):
        if board2[x][0] == board2[x][1] == board2[x][2] and board2[x][0] != '-':
            print('row-----win')

        elif board2[0][x] == board2[1][x] == board2[2][x] and board2[0][x] != '-':
            print('column ---- win')

# elif board2[y][y] == board2[y-1][y +1] == board2[y + 1][y - 1] and board2[y][y] != '-':
#     print('win')

# if board2[0][0] == board2[0][1] == board2[0][2] and board2[0][0] != '-':
#     print('winner')
# if board2[1][0] == board2[1][1] == board2[1][2]and board2[1][0] != '-':
#     print('winner')
# if board2[2][0] == board2[2][1] == board2[2][2]and board2[2][0] != '-':
#     print('winner')
