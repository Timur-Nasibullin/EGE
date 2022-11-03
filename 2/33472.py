for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w <= x) and ((y <= z) == (x <= y)):
                    print(f'{x, y, z, w}')