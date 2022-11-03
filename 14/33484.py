a = 343**6 - 7**10 + 47
n = 0
while a > 0:
    if a % 7 == 6:
        n += 1
    a = a // 7
print(n)
