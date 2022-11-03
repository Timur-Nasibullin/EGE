print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x == (w + y)) or ((w == 0 or z == 1) and (y == 0 or w == 1))):
                    print(x, y, z, w, 0)

