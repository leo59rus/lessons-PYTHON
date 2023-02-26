#создание пустого множества
color = set()

colors = {'blue', 'rose', 'pink'}
print(colors)
 
colors.add('blue') #добавиться, но тк повтор дважды выводитьсчя не бу
print(colors)

colors.add('gray')
print(colors)

colors.remove('rose')#при удалении не существующего будет ошибка
print(*colors)

#удаление с проверкой. если есть удалится. нету пофиг
colors.discard('roseRITO')
colors.discard('pink')
print(colors)

colors.clear()
print(colors)
