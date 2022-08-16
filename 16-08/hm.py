# grades = {3: 33, 11: 100, 1: 15, 12: 99, 9: 44}  # any : any
#
#
# # grades1 =dict(alon=11)
# # grades1['hode'] =55
#
# #
# # grades1 = dict(alon=33, simon=100, igal=99)  # key must be str
# #
# # # print(type(grades))
# # # print(type(grades1))
# # # print(grades1)
# # print(grades)
# #
# # if grades.get('asaf') == None:
# #     grades['asaf'] = 11
# #
# # print(grades)
# #
# # grades['asaf'] = 99
# #
# # print(grades)
# # del grades['asaf']
# #
# # print(grades)
# #
# # print(grades.keys())
# # print(grades.values())
#
# def try_get_value(d1, key):
#     # for k in d1.keys():
#     #     if k == key:
#     #         return d1[k]
#     # return None
#     return d1.get(key)
#
#
# print(try_get_value(grades, 4))
#
#
# def get_sortted_keys(d1):
#     # list_of_keys = []
#     # for k in d1.keys():
#     #     list_of_keys.append(k)
#     # return set(list_of_keys)
#     return set(d1.keys())
#
#
# print(get_sortted_keys(grades))
#
# users1 = {'jack': 1233, 'john': 5677}
# users2 = {'arik': 1765221, 'sveta': 121122}
#
# print(users2)
#
#
# def merge_dict(d1, d2):
#     # for k in users2.keys():
#     #     if not k in  users1.keys():
#     #         users1[k] = users2[k]
#     # return users1
#     # return  users1.update(users2)
#     return users1 | users2  # merge
#
#
# merged = merge_dict(users2, users1)


def sacn_id_name():
    dict1 = {}
    while True:
        id = input('please enter id : ')
        if id == str(-1):
            break
        elif not id in dict1.keys():
            name = input('please enter name : ')
            dict1[id]=name
        else:
            print('this id already exists')

    print(dict1)

sacn_id_name()