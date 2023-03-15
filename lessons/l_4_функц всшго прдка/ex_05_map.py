#с клавы вводится некий набор чисел, в качестве разделителя используется пробел. этот набор чисел будет считан в качестве строки. превратить лист строк в лист чисел

data1 = '1, 2, 3, 4, 5, 6, 66'
data2 = '12 345 55 6 7 88 987 34'

print(data1)
print(data2)
data3 = data1.split(',') #убрад зпт
data4 = data2.split()
print(data3)
print(data4)
#через мап то же самое
data1_1 = list(map(int, data1.split(',')))
print(data1_1)

data2_2 = list(map(int, data2.split()))
print(data2_2)

