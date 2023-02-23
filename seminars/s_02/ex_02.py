# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

n = int(input("vvedite 4islo, ya oredelyu kakoe ono po s4etuv posl. Fibbona4i "))
fib1, fib2, i = 0, 1, 2

while n > fib2:
    fib1, fib2 = fib2, fib2 + fib1
    i+=1

if fib2 != n:
    print("-1")
else:
    print(i)


# if n == sum:
#     print(i)
# else:
#     print(-1)
 #n1=0 n2=1 k=1 a=int(input()) while n2<a:  
 #    n1,n2=n2,n2+n1     k+=1 )