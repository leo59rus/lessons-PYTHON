path = 'file14_03_2023.txt'
my_file = open(path, 'r')
for line in my_file:
    print(line)
my_file.close()