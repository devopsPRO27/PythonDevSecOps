# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#     @property
#     def salary(self):  # getter
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):  # setter
#         self.__salary = value
#
#     # def get_salary(self):
#     #     return self.__salary
#     #
#     # def set_salary(self, new_salary):
#     #     if new_salary < 0:
#     #         self.__salary = 0
#     #     else:
#     #         self.__salary = new_salary
#
#
# emp1 = Employee('john', 133)
# # emp1.set_salary()
# # print(emp1.get_salary())
# print(emp1.salary)
# emp1.salary = 15

class BankAccount:
    def __init__(self, balance, income):
        self.__balance = balance
        self.__income = income

    # def __dict__(self):

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        self.__income = value

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return self.balance < other.balace

    def __ge__(self, other):
        return self.balance >= other.balace

    def __le__(self, other):
        return self.balance <= other.balace

    def __str__(self):
        return f'{self.income}  {self.balance}'


acc1 = BankAccount(2000, 3000)
acc2 = BankAccount(2000, 2000)

print(acc1 == acc2)
print(acc1 > acc2)  # gt
print(acc1 < acc2)  # lt
print(acc1 >= acc2)  # ge
print(acc1 <= acc2)  # le
