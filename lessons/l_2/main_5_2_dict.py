dictionary = {'up': 'вверх', 'down': 'вниз', 'left': 'налево', 'right': 'направо'}
print(dictionary)

for item in dictionary: #item пункт, элт, или в моем случае ключ
    print('{}: {}'.format(item, dictionary[item]))

for (k,v) in dictionary.items():
    print(k, v)# ключ значение