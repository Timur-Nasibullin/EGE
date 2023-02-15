count = 0
for i1 in 'ГЕПАРД':
    for i2 in 'ГЕПАРД':
        for i3 in 'ГЕПАРД':
            for i4 in 'ГЕПАРД':
                for i5 in 'ГЕПАРД':
                    line = i1 + i2 + i3 + i4 + i5
                    if line.count('Г') == 1 and line[0] != 'А' and line[4] != 'Е':
                        count += 1
print(count)