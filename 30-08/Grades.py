import json

dict={'john':100,'roee':99,'josh':42,'michael':100,'kobi':11,
      'shachar':81}

name = input('please enter your name')

print(f'{name} your grade is {dict.get(name)}')