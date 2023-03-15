#составить список пар четное число и его квадрат (четные числа находим в списке)
# l = (1, 2, 3, 5, 8, 15, 23, 38)

# print(l)

# def c(m):
#     res = list()
#     for i in m:
#         if i%2 == 0:
#             res.append((i, i*i))
#     print(res)
# c(l)
#запишем с помощью лямбды

#!!map
def select(f, col):#это встроенная библиотека map
    return [f(x) for x in col] #возвращает список к которому применили функцию ф от икс
#!!map

#!!filter
def where(f, col):#это встроенная библиотека filter
    return [x for x in col if f(x)]#возвращает только те значения которые прощли условие ф от икс
#!!filter

l = (1, 2, 3, 5, 8, 15, 23, 38)
print(l)

res = list(map(int, l))#привели каждое значние к инт
print(res)


res = list(filter(lambda x: x % 2 == 0, res))##возвращает только те значения которые прощли условие x % 2 == 0
print(res)

res = list(map(lambda x: (x, x**2), res))#принимаем икс и возвращаем кортеж(икс, икс в кв, возврат списка)

print(res)