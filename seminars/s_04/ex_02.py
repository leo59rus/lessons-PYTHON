# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

txt = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# x = txt.split()
# c = set(x)

print(len(set(txt.lower().split())))
# len длина(set множество(ткст.уменьшить().разбить на отдельные элты()))

# добавка

txt2 = ""
#с помощью цикла убираем из текста все знаки оставляем только слова
for i in txt:
    if i.isalpha() or i == " ":#i.isalpha() true or false если слово или нет
        txt2 += i


print(txt)
print(txt2)
print(len(set(txt2.lower().split())))