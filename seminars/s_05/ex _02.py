# изменить максимальные оценки на отрицательные
n = int(input("введите колво оценок: "))
list = [int(input(f"введи {i + 1}-ю оценку: ")) for i in range(n)]
x = min(list)
y =max(list)
list2= [x if i == y else i for i in list]
print(list2)
