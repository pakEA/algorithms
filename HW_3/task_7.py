"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и
различаться.
"""

from random import randint, seed

N = 10
a = []
seed(7)

for item in range(N):
    a.append(randint(0, 12))
print(a)

if a[0] > a[1]:
    min_1 = 0
    min_2 = 1
else:
    min_1 = 1
    min_2 = 0

for i in range(len(a)):
    if a[i] < a[min_1]:
        b = min_1
        min_1 = i
        if a[b] < a[min_2]:
            min_2 = b
    elif a[i] < a[min_2]:
        min_2 = i

print(f'Наименьшие числа массива: {a[min_1]} и {a[min_2]}')
