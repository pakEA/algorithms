"""
3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы.
"""
from random import randint, seed

N = 20
a = []
seed(10)

for item in range(N):
    a.append(randint(0, N))

print(a)

max_a = max(a)
min_a = min(a)

idx_max = a.index(max_a)
idx_min = a.index(min_a)

a[idx_max], a[idx_min] = a[idx_min], a[idx_max]

print(a)
