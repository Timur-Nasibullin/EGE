for n in range(1, 10000):
    b = bin(n)[2:]
    sum1 = b[1::2].count('1')
    sum0 = b[0::2].count('0')
    sum = abs(sum1 - sum0)
    if sum == 5:
        print(n)
        break
