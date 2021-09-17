"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием
памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в
виде комментариев к коду. Также укажите в комментариях версию Python и
разрядность вашей ОС.

Python 3.8
Разрядность ОС 64
"""

########################################################################
########################################################################

"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

import sys

TEN = 10

number = int(input('Введите трехзначное число: '))

# цифры вычленяю по одной с конца
num_1 = number % TEN
num_2 = number // TEN % TEN
num_3 = number // TEN ** 2

number_sum = num_1 + num_2 + num_3
number_multiply = num_1 * num_2 * num_3

print(f'Сумма цифр вашего числа: {number_sum}')
print(f'Произведение цифр вашего числа: {number_multiply}')

print(f'Переменная {TEN} занимает - {sys.getsizeof(TEN)} байт')
print(f'Переменная {number} занимает - {sys.getsizeof(number)} байт')
print(f'Переменная {num_1} занимает - {sys.getsizeof(num_1)} байт')
print(f'Переменная {num_2} занимает - {sys.getsizeof(num_2)} байт')
print(f'Переменная {num_3} занимает - {sys.getsizeof(num_3)} байт')
print(f'Переменная {number_sum} занимает - {sys.getsizeof(number_sum)} байт')
print(f'Переменная {number_multiply} занимает - {sys.getsizeof(number_multiply)} байт')

"""
Введите трехзначное число: 666
Сумма цифр вашего числа: 18
Произведение цифр вашего числа: 216
Переменная 10 занимает - 28 байт
Переменная 666 занимает - 28 байт
Переменная 6 занимает - 28 байт
Переменная 6 занимает - 28 байт
Переменная 6 занимает - 28 байт
Переменная 18 занимает - 28 байт
Переменная 216 занимает - 28 байт

Итого было выделено памяти под переменные - 196 бита.

"""

########################################################################

number = input('Введите трехзначное число: ')
number_sum = 0
number_multiply = 1

for digit in number:
    number_sum += int(digit)
    number_multiply *= int(digit)

print(f'Сумма цифр вашего числа: {number_sum}')
print(f'Произведение цифр вашего числа: {number_multiply}')

print(f'Переменная {number} занимает - {sys.getsizeof(number)} байт')
print(f'Переменная {number_sum} занимает - {sys.getsizeof(number_sum)} байт')
print(f'Переменная {number_multiply} занимает - {sys.getsizeof(number_multiply)} байт')

"""
Введите трехзначное число: 666
Сумма цифр вашего числа: 18
Произведение цифр вашего числа: 216
Переменная 666 занимает - 52 байт
Переменная 18 занимает - 28 байт
Переменная 216 занимает - 28 байт

В данном случае память под переменные уже занимает - 108 байта.

Наглядно видно, что переменная типа int занимает 28 байта, а вот
переменная типа str целых 52! Во втором варианте программы 
мы избавились от многих переменных типа int, что позволило нам
уменьшить объем памяти с 196 до 108 байт.
"""

########################################################################
########################################################################

"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0)
и 2 нечетные (3 и 5).
"""

a = int(input('Введите натуральное число: '))

print(f'Переменная {a} занимает - {sys.getsizeof(a)} байт')

even = 0
odd = 0

print(f'Переменная {even} занимает - {sys.getsizeof(even)} байт')
print(f'Переменная {odd} занимает - {sys.getsizeof(odd)} байт')

while a != 0:
    if a % 2:
        even += 1
    else:
        odd += 1
    a = a // 10

print(f'Четных чисел - {even}')
print(f'Нечетных чисел - {odd}')

print(f'Переменная {a} занимает - {sys.getsizeof(a)} байт')
print(f'Переменная {even} занимает - {sys.getsizeof(even)} байт')
print(f'Переменная {odd} занимает - {sys.getsizeof(odd)} байт')

"""
Введите натуральное число: 543673
Переменная 543673 занимает - 28 байт
Переменная 0 занимает - 24 байт
Переменная 0 занимает - 24 байт
Четных чисел - 4
Нечетных чисел - 2
Переменная 0 занимает - 24 байт
Переменная 4 занимает - 28 байт
Переменная 2 занимает - 28 байт

В данной программе видно, что изначально переменные занимают память 76 байт, 
но после всех вычислений объем памяти стал равен 80 байтам. Это все потому что
до того как приступить к вычислениям у нас 1 переменная была отлична от 0, 
а 2 переменные были равны 0, а 0 соответственно занимает 24 байта. После 
проведения вычислений стало наоборот, те 2 переменные уже стали ссылаться 
на значение отличное от нуля, а 3-я переменная стала 0, т.к. мы 'отщипывали'
от нее по одной цифре пока она не стала 0.
"""
