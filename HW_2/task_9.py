"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по
сумме цифр. Вывести на экран это число и сумму его цифр.
"""

num = int(input(f'Введите число: '))

max_num = 0
sum_of_max = 0

while num != 0:
    digits = num
    sum_of_digits = 0

    while num > 0:
        sum_of_digits += num % 10
        num //= 10

    if sum_of_digits > sum_of_max:
        sum_of_max = sum_of_digits
        max_num = digits

    num = int(input(f'Введите число: '))

print(f'Число {max_num} имеет максимальную сумму цифр: {sum_of_max}')
