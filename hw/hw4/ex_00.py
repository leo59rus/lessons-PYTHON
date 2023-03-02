
   #черновичЁк

m = {'1','20','1','5'}
l = list(m)

print(l)

print(type(int(l[0])))
#перевод множества в список, а элт списка в инт

l2 = []
for i in range(len(l)):
    l2.append(int(l[i]))
print(sorted(l2))