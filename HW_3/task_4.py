"""
4. Определить, какое число в массиве встречается чаще всего.
"""

from random import randint, seed

N = 50
a = []
seed(10)

for item in range(N):
    a.append(randint(0, 25))
print(a)

max_frq = 1
num = 0

for i in a:
    frq = 1
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            frq += 1

    if frq > max_frq:
        max_frq = frq
        num = a[i]

print(f'Число {num} повторяется в массиве {max_frq} раз(а).')
