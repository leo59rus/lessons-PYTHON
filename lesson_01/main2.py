#сложение цифр в трехзначном числе
#528 5+2+8
n = 423
summa = 0
while n > 0:
    x = n % 10 #3,2,4
    summa = summa + x
    n = n // 10
print(summa) # 9