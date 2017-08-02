from collections import defaultdict

known_types = ['type1', 'type2', 'type3']

def validation1():
    print('val1')

def validation2():
    print('val2')

def validation3():
    print('val3')

validations = [validation1, validation2, validation3]

dict_type_validation = dict(zip(known_types, validations))

print(dict_type_validation) # {'type1': <function validation1, 'type2': <function validation2, 'type3': <function validation3}

dict1 = {
    "n1": "c1",
    "n2": "c2",
    "n3": "c1",
    "n4": "c3",
    "n5": "c1"
}

dict2 = {
    "n1": "id1",
    "n2": "id2",
    "n3": "id3",
    "n4": "id4",
    "n5": "id5"
}

from collections import defaultdict

result_dict = defaultdict(list)
for key,value in dict1.items():
    result_dict[value].append(dict2[key])
print(result_dict)

exp_dict = {'c1': ['id1', 'id3', 'id5'], 'c2': ['id2'], 'c3': ['id4']}
act_dict = result_dict
print('act_dict', act_dict)
assert act_dict == exp_dict

print('Success!')
