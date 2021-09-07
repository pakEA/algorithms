"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import random

M, N = 5, 4
a = []

for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 10))
    a.append(b)

for item in a:
    print(item)

max_el = 0
for j in range(M):
    min_el = 10
    for i in range(N):
        if a[i][j] < min_el:
            min_el = a[i][j]

    if min_el > max_el:
        max_el = min_el

print(f'Максимальный элемент среди минимальных - {max_el}')
