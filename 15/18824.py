for A in range(128):
    a = True
    for x in range(128):
        for y in range(128):
            if not((x*y < A) or (y > x) or (x >= 8)):
                a = False
    if a:
        print(A)

