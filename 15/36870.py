for A in range(64):
    a = True
    for x in range(64):
        if not(x & 49 != 0 or (x & 28 == 0 or x & A != 0)):
            a = False
    if a:
        print(A)
