'''
В файле содержится последовательность из 10000 целых положительных
чисел. Каждое число не превышает 10000.
Определите и запишите в ответе сначала количество
пар элементов последовательности, у которых сумма нечётна,
а произведение делится на 5, затем максимальную из сумм элементов
таких пар. В данной задаче под парой подразумевается два различных
элемента последовательности.
'''
f = open('17.txt')
numbers = f.readlines()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
count = 0
maxSum = 0
for i in range(10000):
    for j in range(i+1, 10000):
        if (numbers[i] + numbers[j]) % 2 == 1 and \
                (numbers[i] * numbers[j]) % 5 == 0:
            if numbers[i] + numbers[j] > maxSum:
                maxSum = numbers[i] + numbers[j]
            count += 1
print(count, maxSum)




