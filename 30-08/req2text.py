import requests
import json


# Write a python program that sends a GET request to
# json place holder site / users
#
# Convert all the json's to  POPO and save the users
# id and users names in a new file called names.txt

class User1:
    def __init__(self, dict):
        self.__dict__ = dict

    def __str__(self):
        return f'{self.id} hh {self.name}'


try:
    response = requests.get('https://jsonplaceholder.typicode.com/users')
except:
    print('request failed ')
    exit()

print(type(response.text))  # str

list_of_jsons = json.loads(response.text)  # str -> json
print(type(list_of_jsons[0]))  # list of dict
list_of_users = []
for j in list_of_jsons:
    user = User1(j)
    list_of_users.append(user)
print(type(list_of_users[0]))

try:
    file = open('names.txt', 'w')
    for us in list_of_users:
        file.write(f' id = {us.id}  name = {us.name}  \n')
except:
    print('file isn\'t responding')
finally:
    file.close()

