# def my_params(x, y, z=2):
#
#
#     print(x)
#     print(y)
#     print(z)
#
# my_params(55, 23)
#
# def my_params1(*xargs):
#     print(xargs)
#     xargs[1]='alon'
#
# my_params1(2,'hodi','2',15.99)
#

firstname = 'joshoa'
lastname = 'yefah'
age = 19
cars = 20

st1 = ['joshoa', 'yefah', 19, 20]

# key -> value
# 'firstname' : 'jehoshua'
#   'age' : 19

print(st1[2])

# [] ---> list
# () ---> tuple
# {} ---> set
# {key : value ,key : value}
# key = 'age'
# value= 19
#
# st1_dict = {"fname": 'jeshoua', 'age': 19, 2: 'pizza'}
# print(st1_dict['age'])
# print(st1_dict[2])
#
#
# grades = {100 : 'a+' , 95 : 'a', 80 :'b-'}
#
# kobi_grade=95
#
# mtric_to_ft = {1 : 1.6 , 2 : 3.2}
#
# print(grades[kobi_grade])


student1 = {"fname": 'jeshoua', 'age': 19, "fav food": 'pizza'}

print(student1.values())
print(student1.keys())
print(student1.items())

for key in student1 :
    print(f'key = {key} value ={student1[key]}')


for k,v in student1.items():
    print(f'key = {k} and value = {v}')


k,v =('fname' , 'jeshoua')

student1['car'] = 'bugatti'
print(student1)
del student1['age']
print(student1)

