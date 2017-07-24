cars_map = {"BMW": 5, "Audi" : 1, "Lada" : 0}

print(cars_map["Audi"])

del cars_map["Lada"]

cars_map["Audi"] = 2;

print(cars_map.get("Audi"))

print(cars_map.keys())
print(cars_map.values())

for car, carID in cars_map.items():
    print("Car", car, carID)

print("-" * 50 + "THE MAP" + "-" * 50)
print(cars_map)


# -------------- dictionary comprehension --------------
my_dict = {i: i * 2 for i in range(5)} # creates the dictionary with int as a key and its double value as a value
print(my_dict)

for name, value in cars_map.items():
    print(name)
    print(value)

# swapping items in a dictionary
a_dict = {'a': 1, 'b': 2, 'c' : 3}
swapped_dict = {value : key for key, value in a_dict.items()}
print(swapped_dict) # {1: 'a', 2: 'b', 3: 'c'}

# -------------- set comprehension --------------
a_set = set(range(10))
print(a_set)
{item ** 2 for item in a_set}
{item * 3 for item in range(5)} # set comprehension can take not only set as input, but also range() or ay other sequence
some_set = {item * 3 for item in 'abc'}
print(some_set)
some_list = [item * 3 for item in 'abc']
print(some_list)
print('Set type', type(some_set))

