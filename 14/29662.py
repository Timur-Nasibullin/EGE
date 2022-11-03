num = 81**17 + 3**24 - 45
a = 0
while num > 0:
    if num % 9 == 8:
        a += 1
    num = num // 9
print(a)