"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

letter_number = int(input('Введите номер буквы: '))
letter_number = ord('a') + letter_number - 1

print(f'Это буква {chr(letter_number)}')
