# file1 = open('/Users/hothaifa/Desktop/file1.txt','r')

# print(type(file1))
# print(file1.mode)
# print(file1.read()) # reads all the file
# print(file1.read())
# file1.write('jaiobg')
# file1.readline()
# print(file1.readline())
# print(file1.readlines()) # list of lines
# print(file1.readline())
# file1.seek(0)
# print(file1.read(12))
# print(file1.read(1))
# print(file1.tell())


#Write a Python program that takes a
# text file as input and returns the number
# of words of a given text file
# etgar: Some words can be separated by a comma with no space.


filename = input('please enter a file name / path')

file = open(filename,'r')

content =file.read() ## returns the file content

file.close()
content=content.rstrip() ## trim input
content.replace(',',' ')
print(len(content.split(' ')))















