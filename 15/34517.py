for A in range(128):
    f = True
    for x in range(128):
        if not((x & A != 0) <= ((x & 10 == 0) <= (x & 3 !=0))):
            f = False
    if f:
        print(A)













