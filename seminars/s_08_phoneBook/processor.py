def open_file():
    path = open('phoneBook.txt', 'a')
    my_file = open(path, 'r')
    for line in my_file:
        print(line)
    my_file.close()
    
    

def get_contacts() -> list:
    return 1

def save_file():
    contacts = dict()
    name = input("введите фамилию - ")
    number = input(f"введите номер телефона для фамилии {name} - ")
    contacts[name] = number
    print(contacts)
    #записать это в файл
    
    
#     data = open('phoneBook.txt', 'a')#создали переменную дата для добавления 
# #в ней мы открываем и автоматически создаём тк не существует файл ткст
# #при добавленеии текстс файла не удаляется а прибавляется
#     data.writelines(contacts)
#     data.writelines(name)
#     data.writelines(number)# запись в дату колорс, элты без разделителей сплошником
#     data.close()#закрываем файл ткст после работы с ним
    with open('phoneBook.txt', 'w') as data:
        data.write(contacts)
        data.write('\n')
    
   
    