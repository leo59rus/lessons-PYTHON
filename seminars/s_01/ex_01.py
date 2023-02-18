# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750

# import math

# print("задача №1")

# print("skol'ko km proezjaet mashina v den'? vvedite: ")
# n = int(input())
# print("skol'ko km sostavlyaet marshrut? vvedite: ")
# m = int(input())

# print("mashina proedet marshrut za ", math.ceil(m/n), " dnei ")

n = 700
m = 700

a1 = m//n

a2 = bool(m%n)#остаок есть значит тру, тру это один в цифрах
print(a2)
a2 = int(a2)
print(a2)
result = a1 + a2
print(result)

