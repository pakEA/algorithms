"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным
и максимальным элементами. Сами минимальный и максимальный элементы в сумму
не включать.
"""

from random import randint, seed

N = 10
a = []
seed(6)

for item in range(N):
    a.append(randint(0, 12))
print(a)

sum_of_nums = 0
idx_max_num = a.index(max(a))
idx_min_num = a.index(min(a))

if idx_max_num < idx_min_num:
    idx_max_num, idx_min_num = idx_min_num, idx_max_num

print(sum(a[idx_min_num + 1:idx_max_num]))
