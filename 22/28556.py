def f(x):
    a = 0
    b = 0
    while x > 0:
        a += x % 8
        b += 1
        x = x // 8
    return a * b


for i in range(10000):
    if f(i) == 24:
        print(i)
