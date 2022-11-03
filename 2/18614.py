print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x, y, z, w, end=' ')
                if ((w == 0 or x == 0) == (z == 0 or x == 1)) and (y == 1 or w == 1):
                    print(1)
                else:
                    print(0)
