a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} сложение
i = a.intersection(b) # i = {8, 2, 5}  пересечение
dl = a.difference(b) # dl = {1, 3} delete
dr = b.difference(a) # dr = {13, 21} delete
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

a = {1, 8, 7}
b = frozenset(a) #неизменяемое замороженное множество
print(b)