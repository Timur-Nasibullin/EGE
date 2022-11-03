for a in range(65):
    f = True
    for x in range(65):
        if not(x & 41 == 0 or x & 33 != 0 or x & a != 0):
            f = False
    if f:
        print(a)
        break
