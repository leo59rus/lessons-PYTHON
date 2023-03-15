def calc1(a, b):
    return a + b
def calc2(a, b):
    return a * b

def math(operation, x, y):# в функции вызывается фцнкция
    print(operation(x, y))
#math(calc1, 2)
#math(calc2, 3)

# lambda
calc3 = lambda a, b: a // b

math(calc3, 10, 2)

math(lambda a, b: a - b, 10, 2)#сразу записали функцию в принте с помощью ламбда