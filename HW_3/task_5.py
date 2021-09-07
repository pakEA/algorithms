"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
"""

from random import randint, seed

N = 50
a = []
seed(1)

for item in range(N):
    a.append(randint(-25, 25))
print(a)

max_negative = min(a)
idx_max_negative = a.index(max_negative)

print(f'Максимальный отрицательный элемент {max_negative} и его '
      f'индекс {idx_max_negative}')
