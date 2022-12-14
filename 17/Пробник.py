# Определите количество пар последовательности, в которых
# хотя бы одно число делится на 3, а сумма элементов пары не более
# максимального элемента последовательности, кратного 3.
# В данной задаче под парой подразумевается два идущих подряд
# элемента последовательности.

# Функция для открытия файла
f = open('Пробник.txt.txt')
# Чтение всех строк из файла в массив строк
list = f.readlines()
# Преобразование каждой строки и число
for i in range(len(list)):
    list[i] = int(list[i])
x = 0
count = 0
y = 0
# Поиск максимального элемента кратного 3
for i in range(len(list)):
    if list[i] > x and list[i] % 3 == 0:
        x = list[i]
# Решение задачи по основному условию
for i in range(len(list) - 1):
    if (list[i] % 3 == 0 or list[i + 1] % 3 == 0) and (list[i] + list[i + 1] <= x):
        count += 1
        if list[i] + list[i + 1] > y:
            y = list[i] + list[i + 1]
print(count, y)

