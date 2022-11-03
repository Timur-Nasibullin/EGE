n = 0
m = 0
f = open('37372.txt')
a = list(map(int, f.readlines()))
for i in range(10000):
    for y in range(i+1, 10000):
        if abs(a[i] - a[y]) % 45 == 0 and (a[i] % 18 == 0 or a[y] % 18 == 0):
            n += 1
            if (a[i] - a[y]) > m:
                m = (a[i] - a[y])
print(n, m)



