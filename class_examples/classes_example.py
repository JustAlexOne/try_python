class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound


    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

#inherits the class Animal
class Dog(Animal):

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

    def get_sound(self):
        return self.__sound

spot = Dog("Spot", 53, 27, "Ruff", "JustAlex")

