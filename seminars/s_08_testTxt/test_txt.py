myFile = open('test1.txt')
print(myFile.read())
myFile.close()


path = 'test1.txt'
my_file = open(path, 'r')
for line in my_file:
    if line == 'запись':
        print(line)

    
my_file.close()




