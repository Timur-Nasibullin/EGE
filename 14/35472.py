alph = '0123456789ABCDEFGHI'
n = 729**7 + 3**16 - 18
base = 9

res = ''
while n > 0:
    res += alph[n % base]
    n //= base

print(res[::-1].count('0'))