import os

mac='ls >> content.txt'

date_command = os.system('date >> content.txt')
date_command = os.system(mac)

if date_command != 0:
    print('Error Exit Code ==' ,date_command)
