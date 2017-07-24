print(True + False) # 1 = 1 + 0
print(True + True) # 2 = 1 + 1

print(type(1)) # <class 'float'>
print(isinstance(1, float)) # False
print("It is", type(1.0) == float, "float", "yes", "not") # It is True float yes not

a = 10
print(isinstance(a, int))

a = "Some string"
print(isinstance(a, str))

a = 2.8
print(isinstance(a, float))

# int() will trancate, not round
print(int(2.8)) # 2

print(11 % 2) # 1
