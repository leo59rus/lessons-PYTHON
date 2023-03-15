def find_farthest_orbit(orbits):
    return max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1])
    #(1, 3) тру*1*3
    #(2.5, 10) тру*2.5*10  >>>> MAX
    #(7, 2), тру*7*2
    #(6, 6), False(0) * 6*6 = 0
    #(4, 3) тру ,,,
    #макс элт массива(тру либо фолс перемноженный с элтом ккортежа)
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


print(*find_farthest_orbit(orbits))