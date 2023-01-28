"""
Задание 5
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. Далее эта запись обрабатывается по следующему правилу:
а) если число чётное, то к двоичной записи числа слева дописывается 10;
б) если число нечётное, то к двоичной записи числа слева дописывается 1 и справа дописывается 01.
Полученная таким образом запись является двоичной записью искомого числа R.
Укажите минимальное число N, после обработки которого с помощью этого алгоритма получается число R, большее, чем 441.
В ответе запишите это число в десятичной системе счисления.
"""
# Решаем методом подбора
for i in range(1, 1000):
    # bin(n) переводит число n в двоичную систему счисления
    # [2:] т.к. число представляется в виде '0b0101110', то необходимо убрать первые два ненужные символа
    b = bin(i)[2:]
    sum = b.count('1')
    b += str(sum % 2)
    sum = b.count('1')
    b += str(sum % 2)
    # int(<строка>, <система ИЗ которой переводим>) - переводит строку из любой системы в десятичную
    r = int(b, 2)
    if r > 396:
        print(r)