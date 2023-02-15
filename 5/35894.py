for i in range(105, 1000):
    b = bin(i)[2:]
    for j in range(3):
        sum1 = b.count('1')
        sum0 = b.count('0')
        if sum1 == sum0:
            b += b[-1]
        else:
            if sum1 > sum0:
                b += '0'
            if sum1 < sum0:
                b += '1'
    a = int(b, 2)
    if a % 4 == 0:
        print(i)
        break


