import glob
import os

import time

test_file = open("test.txt", "wb")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("Hello to the file\n", 'UTF-8'))
test_file.close()

test_file = open("test.txt", "r+")

text_in_file = test_file.read()

print(text_in_file)
test_file.close()
#open and auto-close
with open("test.txt", "w") as test_file:
    test_file.write("My name is {0}".format("JustAlex"))

os.remove("test.txt")

print(os.getcwd()) # current working directory

my_path = os.path.join('/Users/Oleksii_Cherevatyi/Projects/PythonTest', 'hello_python.py')
print(my_path)
# returns /Users/Oleksii_Cherevatyi/Projects/PythonTest/hello_python.py

print(os.path.split(my_path)) # ('/Users/Oleksii_Cherevatyi/Projects/PythonTest', 'hello_python.py')
(dir_path, filename) = os.path.split(my_path)
print(dir_path) # /Users/Oleksii_Cherevatyi/Projects/PythonTest
print(filename) # hello_python.py

(shortname, extension) = os.path.splitext(filename)
print(shortname) # hello_python
print(extension) # .py

files_in_cwd = glob.glob(os.getcwd() + '/*.py') # all files with .py extension inside the curernt folder
print(files_in_cwd)

print(*files_in_cwd, sep='\n') # prints each list item in new line

print(*glob.glob('*example*'), sep='\n')

metadata = os.stat('hello_python.py')
print(metadata)
print(metadata.st_mtime)

print(time.localtime(metadata.st_mtime))

print(os.path.realpath('hello_python.py')) # the absoulte path to the file

print(*[os.path.realpath(file) for file in glob.glob('*.py')], sep='\n')
# creates an absolute path's for all files inside the current directory, ending with .py
