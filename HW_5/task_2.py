"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict
from functools import reduce

dict_of_nums = defaultdict(list)

nums = input('Введите два 16-ричных числа через пробел: ').split(' ')

for item in nums:
    dict_of_nums[item.upper()] = list(item.upper())

print(dict_of_nums)

# переводим в десятичную систему и находим сумму
sum_of_nums = sum([int(''.join(i), 16) for i in dict_of_nums.values()])
# полученную сумму снова переводим в 16-ричную систему и отбрасываем ненужные фрагменты
sum_in_hex = hex(sum_of_nums).split('0x')[1]

print(f'Сумма: {sum_in_hex.upper()}')

# по аналогии с суммой переводим в десятичную систему и производим умножение
mult_of_nums = reduce(lambda x, y: x * y, [int(''.join(i), 16)
                                           for i in dict_of_nums.values()])
mult_in_hex = hex(mult_of_nums).split('0x')[1]

print(f'Произведение: {mult_in_hex.upper()}')
