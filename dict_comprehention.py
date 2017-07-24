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

