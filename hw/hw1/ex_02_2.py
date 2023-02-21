# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

#result = x + x + (x * 4)
print("введите общее количество журавликов: ")
result = int(input()) 

if result%6 == 0:
    count = 1
    while result != count * 6:
            count += 1
            if result == count*6:
                print(f"Петя и Сережа сделали по {count} журавлика(ов), а Катя {count * 4} журавлика(ов)")
else:
    print("вы ввели неправильные данные")                