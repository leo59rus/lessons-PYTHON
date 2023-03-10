# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму
# двух целых неотрицательных чисел. Из всех арифметических операций
#  допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#  4 

# def sum(a, b):
    
#     if a == 0:
#         return b
#     return sum(a - 1, b + 1)
# print(sum(2, 4))


def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)
print(sum(5,15))

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 



# a = int(input("a = "))# A = 2; 
# b = int(input("b = "))# B = 3 

# def func(a, b):#1/ 2,3   2/ 2,2  3/2,1
#     if b == 1:#1/no     2/no     3/yes
#         return a#                3/ a = 2
#     if b != 1:#1/yes    2/yes
#         return (a * func(a, b - 1))#1-> 2 * func(2, 2){2 * (2*2)}  2-> 2 * func(2, 1) {2 * 2}
    
# print(func(a, b)) #-> 8

# sam
# a = int(input("a - "))
# b = int(input("b - "))

# def stepen(a, b):
#     if b == 1:
#         return a
#     return a * stepen(a, b - 1)
# print(stepen(2, 3))