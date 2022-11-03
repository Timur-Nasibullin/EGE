'''
В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
Определите и запишите в ответе сначала количество пар элементов последовательности,
разность которых четна и хотя бы одно из чисел делится на 31, затем максимальную из сумм элементов таких пар.
В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.
'''

x = 0
oldx = int(input())
count = 0
for i in range(10000 - 1):
    x = int(input())
    if abs(oldx - x) % 2 == 0 and (oldx % 31 == 0 or x % 31 == 0):
        # count += 1
        count = count + 1
    oldx = x
print(count)