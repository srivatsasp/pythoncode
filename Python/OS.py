
import os
import datetime

print(os.getcwd())
cwd = os.getcwd()
print(dir(os))

print(os.stat('/Users/srivatsa/Desktop/Python'))
# print(datetime.fromtimestamp(1541252621))
print(datetime.datetime.fromtimestamp(1541252621))

# print(dir(datetime))

path, ext = os.path.splitext('/Users/srivatsa/Desktop/Python/temp.txt')
print(ext)
