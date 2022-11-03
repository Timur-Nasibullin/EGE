print('x', 'y', 'z', 'w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x == 1 or y == 0) and (w != z) and w == 1:
                    print(x, y, z, w)