"""
Определить количество различных подстрок с использованием хеш-функции.
Задача: на вход функции дана строка, требуется вернуть количество различных
подстрок в этой строке.

Примечание: в сумму не включаем пустую строку и строку целиком.
"""
import hashlib


def hash_func(string):
    length = len(string)
    hash_set = set()

    for i in range(length - 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)


if __name__ == '__main__':
    a = 'man'
    print(hash_func(a))  # 5
