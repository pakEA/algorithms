"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы, в
другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком
сложно, то используйте метод сортировки, который не рассматривался на уроках.
"""

from random import randint

M = 5
my_arr = [randint(0, 100) for _ in range(2 * M + 1)]
# right = []  # закомментированный код нужен если надо сохранить числа
print(my_arr)

while len(my_arr) > M + 1:
    max_el = max(my_arr)
    # right.append(max_el)
    my_arr.remove(max_el)

median = max(my_arr)
# print(my_arr)
print(f'Медиана:  {median}')
# print(right)

"""
Данный алгоритм заключается в том, чтобы искать максимальные элементы
в массиве до тех пор пока длина массива не станет равной натуральному
числу M + 1. Как только достигнется это условие, мы берем максимальный
элекмент в массиве, который и будет нашей медианой.
"""
