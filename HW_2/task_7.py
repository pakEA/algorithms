"""
7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n -
любое натуральное число.
"""

a = 141
result_left = 0

result_right = a * (a + 1) / 2

for item in range(1, a + 1):
    result_left += item

print('%d = %d' % (result_left, result_right))
