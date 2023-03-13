# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 



a = int(input("a = "))
b = int(input("b = "))

def func(a, b):
    if b == 1:
        return a
    if b == 0 or a == 1 or a == 0:
        return 1
    return a * func(a, b - 1)
    
print(func(a, b))
