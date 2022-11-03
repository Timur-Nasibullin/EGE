s = 1
while True:
    a=0
    b=1
    x = s
    while x > 0:
        if x%2 > 0:
            a += x%12
        else:
            b *= x%12
        x = x // 12
    if a == 2 and b == 10:
        break
    s += 1
print(s)