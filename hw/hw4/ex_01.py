# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

#23.55 seminar 5 razbor
n1 = int(input("введи колво элтов 1го мнжства: "))
n2 = int(input("введи колво элтов 2го мнжства: "))
m1, m2 = [], []
for i in range(n1):
    m1.append(input(f"вводи {i + 1} элт 1го множества: "))

for i in range(n2):
    m2.append(input(f"вводи {i + 1} элт 2го множества: "))
print(m1)
print(m2)

resultSet = set()
if n1 >= n2:
    for i in m1:
        for item in m2:
            if item == i:
                resultSet.add(i)
             
else:
    for i in m2:
        for item in m1:
            if item == i:
                resultSet.add(i)
result = list(resultSet)

resultSorted = []
for i in range(len(result)):
    resultSorted.append(int(result[i]))

	

print(sorted(resultSorted))

