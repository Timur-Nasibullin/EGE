m = 1000
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    r = int(s, 2)
    if r > 52:
        m = min(m, r)
print(m)