# Найти максимальное значение x 
# при котором программа печатает сначала 4 а затем 5
for x in range(10000, 0, -1):
    y = x
    Q = 9
    L = 0
    while x >= Q:
        L = L + 1
        x = x - Q
        M = x
    if M < L:
        M = L
        L = x
    if L == 4 and M == 5:
        print(y)
