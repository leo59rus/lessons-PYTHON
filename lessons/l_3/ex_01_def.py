def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)
sum_numbers(1)
sum_numbers(2)
sum_numbers(3)
sum_numbers(4)
sum_numbers(5)

def sum_str(*args):
    res = ""
    for i in args:
        res += i
    print(res)
sum_str("a", "b", "c")
sum_str("a", "b", "cft", "[p")