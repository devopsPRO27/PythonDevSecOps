from pathlib import Path

# path = Path("/Users/hothaifa/Desktop/chromedriver")
#
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.name)
# path.mkdir()

file1 = open('/Users/hothaifa/Desktop/urii.txt','w')
for i in range(100):
    file1.write('how you doin :( ??')
file1.close()