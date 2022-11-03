print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((x == 0 or y == 1) == (z == 0 or w == 1)) or (x == 1 and w == 1)):
                    print(x, y, z, w, 0)
