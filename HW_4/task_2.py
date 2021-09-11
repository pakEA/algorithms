"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import cProfile

N = 10000

a = [i for i in range(N)]
print(a)


def with_eratosthenes(lst, n):  # алгоритм с использованием решета Эратосфена
    lst[1] = 0
    m = 2

    while m < n:
        if lst[m] != 0:
            j = m * 2
            while j < n:
                lst[j] = 0
                j += m
        m += 1
    b = [i for i in a if i != 0]
    return b


def without_eratosthenes(n):  # алгоритм без использования решета Эратосфена
    idx = 2
    b = []
    count = 0
    for i in range(idx, n + 1):
        for j in range(idx, i):
            if i % j == 0:
                count += 1

        if count == 0:
            b.append(i)
        else:
            count = 0
    return b


def main():
    with_eratosthenes(a, N)
    without_eratosthenes(N)


cProfile.run('main()')

"""
Преимущество решения данной зачади однозначно будет за алгоритмом решета
Эратосфена, т.к. в данном алгоритме оценка сложности будет О(n) - линейная.
А вот уже второй алгоритм будет иметь сложность О(n^2) - квадратичная, т.к. 
увеличивая список на порядок, время выполнения алгоритма увеличивается в 100 раз.
"""
