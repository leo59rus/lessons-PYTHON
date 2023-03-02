# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("введите колво элтов: -- "))
a = []
for i in range(n):
    a.append(int(input(f"введите {i + 1} элт массива: -- ")))

x = int(input("введи число для поиска самого близкого по величине элемент: -- "))   


dict = {} # библиотека ключ разница    value-элт массива
for i in range(n):
    # if x - a[i] < 0:
    #     t = (x - a[i]) * -1
    #     dict[int(t)] = a[i] #key-разница    value-элт массива 

    # else:
    #     t = x - a[i]
    #     dict[int(t)] = a[i]  #key-разница    value-элт массива
    # вместо верхнего применяем ABSolute
    t = abs(x - a[i]) #ABSolute
    dict[int(t)] = a[i]
     

listKey = [] # создание листа ключей
for item in dict:
    listKey.append(int(item))

# вывод вложения с минимальным значением ключа
print(dict[min(listKey)]) 
"""
keyMin = int(listKey[0])

print(type(listKey[0]))
print(type(keyMin))

for i in range(len(listKey)):
    print(type(listKey[0]))
    print(type(keyMin))
    if listKey[i] < keyMin:
        keyMin = listKey

# print(d['w']) # вывод вложения по ключу
print(dict[str(keyMin)])
 
"""


#создание ключа с вложениями
# d['q'] = 'qwerty', 'ytrewq'
# d['w'] = 'werty'

# print(d) #вывод всего списка с ключами и вложеними
# print(*d) #вывод ключей

# print(d['w']) # вывод вложения по ключу

# #удаление ключа и всех его вложений
# del d['w']
# print(d)
# for item in dictionary: #item пункт, элт, или в моем случае ключ
#     print('{}: {}'.format(item, dictionary[item]))

# for (k,v) in dictionary.items():
#     print(k, v)# ключ значение