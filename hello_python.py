import random
import sys
import os

import time
from datetime import datetime

print("Hello World")

#Comment
'''
Multiline
comment
'''
name = "JustAlex"
print(name)

a = 5;
b = 10;
c = a * b;

print(c)
print(5 / 2) # returns 2.5
print(5 // 2) # returns 2
print("the result is", b)

print("%s %s %s" % ("A", "B", "C"))

#new lines
print("I don't like ", end="")
print("newlines")

#5 new lines
print('\n' * 5)
print("finish")

current_milli_time = lambda: int(round(time.time() * 1000))
current_milli_time2 = lambda: (round(time.time() * 1000000))

print(1496756227107245)
print(current_milli_time2())
dt = datetime.now()
print(dt.timestamp())

size = 10
other = 20 if size > 5 else 100
print(other)
print(__name__)

a = 10
print(a)

a = "I am String now"
print(a)

a = True
print(a)

b = 3/4
print(b)

list = [4, 2, 7, 8, -1, 0, 34, 67, 34]
print(list)

print("It is", type(1.0) == float, "float", "yes", "not") # It is True float yes not