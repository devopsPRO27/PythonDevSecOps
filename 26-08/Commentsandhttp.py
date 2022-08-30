import requests


class Comment:
    def __init__(self, dict):
        self.__dict__ = dict


response = requests.get('https://jsonplaceholder.typicode.com/comments')

if response.ok:
    comments = response.json()  # list of dicts

    print(comments[3]['body'])

    comment1 = comments[0]  # dict
    comment1_obj= Comment(comment1)
    print(comment1_obj.body)