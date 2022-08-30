import requests
#
# res = requests.get('https://google.com/hfgiaeuofghvadso')
#
# # print(res)  # <Response [200]> as str
# # print(res.text)  # page source code
# print(res.url)
# print(res.ok)
# print(res.status_code)
#
# if 200 <= res.status_code < 300:
#     print('its working success ')
# else:
#     print('something went wrong ')




class User:
    def __init__(self,dict):
        self.__dict__=dict


jph_response= requests.get('https://jsonplaceholder.typicode.com/users')

if not jph_response.ok:
    exit()
# print(jph_response.text)
print(type(jph_response.text))
print(jph_response.text[1])

users_dict = jph_response.json()
print(type(users_dict))
print(users_dict[0]['name'])
users_objects=[]

for user in users_dict :
    temp = User(user)
    print(type(temp))
    users_objects.append(temp)

for obj in users_objects:
    print(obj.name)

users_objects[3].name =  'new name '
for obj in users_objects:
    print(obj.name)

for i in users_objects:
    if len(i.username) > 10 :
        print('we got it ' + i.username)

print(i.address['geo']['lat'])