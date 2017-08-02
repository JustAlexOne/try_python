import random

for x in range(0, 10):
    print(x, ' ', end="")

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300], [1000, 2000, 30000]]

for x in range(0, 4):
    for y in range(0, 3):
        print(num_list[x][y])

random_num = random.randrange(0, 10)
while(not(random_num == 5)):
# while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,10)

some_list = [
    "A",
    "A",
    "B",
    "C",
]

for index, element in enumerate(some_list):
    print('{0} {1}'.format(index, element))