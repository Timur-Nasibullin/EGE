for A in range(1000):
    n = True
    for x in range(1000):
        for y in range(1000):
            if not((x + 2*y < A) or (y > x) or (x > 30)):
                n = False
    if n:
        print(A)






