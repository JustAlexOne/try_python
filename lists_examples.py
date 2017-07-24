import random
import sys
import os

import _thread
import threading
from time import sleep

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

print("First item is", grocery_list[0])

grocery_list[0] = "Green Juice"
print("First item is", grocery_list[0])

# print first 2 items
print(grocery_list[0:2])

grocery_list.append("Onions")

for grocery in grocery_list:
    print(grocery)

grocery_list.insert(0, "Apples")

print(grocery_list)
grocery_list.remove("Apples")

grocery_list.sort()

grocery_list.reverse()

print(grocery_list)

#remove item from list by index
del grocery_list[0]
print(grocery_list)

#length
print(len(grocery_list))

#max item
print(max(grocery_list))

#min item
print(min(grocery_list))

#combine lists

second_list = ["BMW", "Audi", "Mercedes"]

combined_list = grocery_list + second_list

print("Combined list", combined_list)

my_list = ['a', 'b', 'c']
list2 = ['a', 'b', 'c']


my_list.append(True);

print("List 1", my_list)

# search for values in a list

my_list = ['a', 'b', 'c', 'd', 'a']
print(my_list.count('a')) # 2

d = 'd'

'a' in my_list # True!!!!!!!!!!!!

if d in my_list:
    indexD = my_list.index(d)
    print(f"index of {d} is {indexD}")

indexA = my_list.index('a', 3)

my_list.remove('a')

my_list.pop() # removes last item and returns it

my_list.pop(0) # removes first item and returns it

# ------------------------------ Tuples ------------------------------

some_tuple = ('Audi', 'BMW', 'Hyundai') # tuple is an immutable list

my_list = ['a', 'b', 'c']

new_tuple_out_of_list = list(some_tuple)
new_list_out_of_tuple = tuple(my_list)

not_a_tuple = ('a')

print(type(not_a_tuple)) # <class 'str'>

a_tuple = ('a',)
print(type(a_tuple)) # <class 'tuple'>


# assign multiple vars at once (with help of tuple)
v = ('a', True, 3)

(a_string, b_bool, c_int) = v

print(a_string) # a
print(b_bool) # True
print(c_int) # 3

# shorter
(a_string, b_bool, c_int) = ('a', True, 3)

# usage
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)

# ------------------------------ List Comprehensions ------------------------------

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled_list = [elem * 2 for elem in a_list]
print(doubled_list) # [2, 4, 6]

[elem * 2 for elem in a_list] # just returns a doubled list (not modifying the root list)

doubled_only_even_numbers = [elem * 2 for elem in a_list if elem % 2 == 0]
print('doubled_only_even_numbers', doubled_only_even_numbers)

