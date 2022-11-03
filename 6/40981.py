def f(s):
    s = s // 10
    n = 1
    while s < 221:
        if n % 2 == 0:
            s = s + 13
        n = n + 5
    return n
for i in range(10000):
    if f(i) == 121:
        print(i)


