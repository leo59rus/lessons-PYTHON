list = [1, 2]
print(list)
list.append(4)#добавлениеи в конец списка
print(list)

list2 = []
for i in range(10):
    list2.append(i + 1)
print(list2)

list2.pop() #удаление последнего элта
print(list2)
print(list2.pop())#выведение удаляемого элта и удаление его с листа
print(list2)

a = list2.pop()#удаление последнего элта листа и присвоение его к переменной а
print(list2, a)

list2.pop(3)#удадение 3го элта - 4ки
print(list2)

list2.insert(3, 44)#на 3ю позицию вствляем элт 4
print(list2)


