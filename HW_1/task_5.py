"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита
они стоят, и сколько между ними находится букв.
"""

first_letter = ord(str.lower(input('Введите 1-ю букву: ')))
second_letter = ord(str.lower(input('Введите 2-ю букву: ')))

first_letter = first_letter - ord('a') + 1
second_letter = second_letter - ord('a') + 1

print('Места в алфавите: "%d" и "%d"' % (first_letter, second_letter))
print(f'Между ними букв: {abs(first_letter - second_letter) - 1}')
