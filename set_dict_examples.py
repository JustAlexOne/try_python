a_set = {1, 2, 3}

# convert to set
set([5, 6, 7])

empty_set = set()

empty_dictionary = {}

# clear set
a_set.clear()

a_set = {1, 2, 3}
print(a_set)
2 in a_set # True

my_set_1 = {1, 2}

my_set_2 = {1, 2, 3}

print("Union set", my_set_1.union(my_set_2)) # 1, 2, 3

my_set_1.issubset(my_set_2) # True
my_set_2.issuperset(my_set_1) # True

# ------------------------------ Dictionaries ------------------------------
my_dict = {'car1': 'Audi', 'car2': 'BWM'}
print('my_dict', my_dict)

print(my_dict['car1']) # Audi

print(len(my_dict)) # 2

# adding items to dict

my_dict['car3'] = 'Mercedes'

print(my_dict)