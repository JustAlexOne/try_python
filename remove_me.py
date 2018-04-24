def func(name, age=5):
    print('name', name)
    print('age', age)


func("me", 10)

func("me", 5)
age = None
func("me", age=age)
