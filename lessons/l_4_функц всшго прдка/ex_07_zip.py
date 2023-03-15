users = ['petr', 'fil', 'roma']
ids = [1, 2, 3]
salary = [10000, 20000]
data = list(zip(ids, users))
print(data)#(1, 'petr'), (2, 'fil'), (3, 'roma')

data2 = list(zip(ids, users, salary))
#вывод по колву из минимального списка
print(data2)#(1, 'petr', 10000), (2, 'fil', 20000)
