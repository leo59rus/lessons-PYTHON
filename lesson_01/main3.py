i = 0
while i < 5:
    i = i + 1
else:
    print('Пожалуй')
    print('хватит )')
print(i)

print("continue  ... нахождение минимального делителя для введённого числа")

n = int(input())
flag = True
i = 2
while flag: #пока флаг тру
    if n % i == 0: #если остаток от деления равен 0
        flag = False
        print(i) 
    elif i > n // 2: #делитель числа не может превышать введенное число, деленное
                     #на 2  
        print(n)
        flag = False
    i += 1

r = range(100, 0, -20) # от 100 до 0 ,шаг -20
for i in r:
     print(i)

for i in 1, -2, 3, 14, 5: #печать всех по очереди
    print(i)

for i in "qwerty":
    print(i)


a = "qwertyuiop"
print(a[1])

