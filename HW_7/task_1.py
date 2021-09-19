"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в виде
функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint

my_arr = [randint(-100, 100) for _ in range(50)]

print(my_arr)


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return arr


if __name__ == '__main__':
    print(bubble_sort(my_arr))
