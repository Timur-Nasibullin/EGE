z = 0
m = 0
f = open('39764.txt')
n = f.readlines()
arr = []
for i in range(len(n)):
    arr.append(int(n[i]))
for i in range(len(arr) - 2):
    a = arr[i]
    b = arr[i + 1]
    c = arr[i + 2]
    h = max(a, b, c)
    k1 = min(a, b, c)
    k2 = a + b + c - h - k1
    if h**2 == k1**2 + k2**2:
        z += 1
        if a + b +c > m:
            m = a + b + c
print(z, m)






