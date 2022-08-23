class bit:
    '''this is the bit class'''

    def __init__(self, number):
        self.number = number

    def calc_bits(self):
        return self.number


class byte(bit):
    def __init__(self, number):
        super().__init__(number)

    def calc_bits(self):
        return self.number * 8


class kb(bit):
    def __init__(self, number):
        super().__init__(number)

    def calc_bits(self):
        return self.number * 1024 * 8


class mb(bit):
    def __init__(self, number):
        super().__init__(number)

    def calc_bits(self):
        return self.number * 1024 * 1024 * 8


class gb(bit):
    def __init__(self, number):
        super().__init__(number)

    def calc_bits(self):
        return self.number * 1024 * 1024 * 1024 * 8



print('please enter a number and a unit [bit ,byte , kb ,mb ,gb]')
number = int(input())
unit = input()
units={'bit':bit(number),'byte':byte(number),\
       'kb':kb(number),'mb':mb(number),'gb':gb(number)}
print(units[unit].calc_bits())


# if unit == 'bit':
#     my_unit = bit(number)
# elif unit == 'byte':
#     my_unit = byte(number)
# elif unit == 'kb':
#     my_unit = kb(number)
# elif unit == 'mb':
#     my_unit = mb(number)
# elif unit == 'gb':
#     my_unit = gb(number)
#
# print(my_unit.calc_bits())
#
