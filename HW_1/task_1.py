"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

TEN = 10

number = int(input('Введите трехзначное число: '))

# цифры вычленяю по одной с конца
num_1 = number % TEN
num_2 = number // TEN % TEN
num_3 = number // TEN ** 2

number_sum = num_1 + num_2 + num_3
number_multiply = num_1 * num_2 * num_3

print(f'Сумма цифр вашего числа: {number_sum}')
print(f'Произведение цифр вашего числа: {number_multiply}')
