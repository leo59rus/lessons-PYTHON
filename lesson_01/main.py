a = 5
b = 2.2
c = "cool"
print(a, "-", b, "-", c)
print(f"{a} - {b} - {c}") # to ze samoe
print("{} - {} - {}".format(a,b,c)) # to ze samoe
print("введите перое число: ")
d = input()# ввод  с консоли переменной a
print(type(d))


e  = input("введите второе число: ")
f = int(d)
g = int(e)
print(d ," + ", e, " = ", f + g)
print(type(d))

v = 7.678
j = 9.78686
print(round(v*j, 2))

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)