# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
#  Счастливым билетом называют такой билет с шестизначным
#   номером, где сумма первых трех цифр равна сумме 
#   последних трех. Т.е. билет с номером 385916 – 
#   счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
#    программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


ticket = int(input("введите 6ти значный номер билета: "))
# НЕ РАБОТАЕТ(((
##n = [int(i) for i ticket]:
# for i in ticket:
#     if sum(i[:3]) == sum(i[3:]):
#         print("Yes")
#     else:
#         print("no")

