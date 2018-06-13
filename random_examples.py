import random

cars = ['audi', 'bmw', 'aston marting', 'mercedes', 'skoda', 'vw']

random_car = random.choice(cars)

print(random_car)

assert random_car in cars