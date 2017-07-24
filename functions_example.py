def addNumber(num1, num2):
    sumNum = num1 + num2
    return sumNum

print(addNumber(1, 4))


def printB():
    print('I am B')

def printA():
    print('I am A')



options = {
    1 : printA,
    2 : printB
}

options[2]()