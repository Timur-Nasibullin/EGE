for a in range(1, 63):
    f = True
    for x in range(1, 63):
        if not((x & 33 != 0) or (x & 45 == 0) or (x & a != 0)):
            f = False
    if f:
        print(a)
        break

