"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

N = int(input('Введите количество предприятий: '))

ENTERPRISE = namedtuple('Enterprise', 'name, quarter_1 quarter_2 quarter_3 '
                                      'quarter_4')

enterprise_profit = {}

for i in range(N):
    enterprise_name = input('Введите название предприятия: ')
    profit_lst = input('Введите прибыль за каждый квартал через пробел: ').split(' ')
    enterprise = ENTERPRISE(
        name=enterprise_name,
        quarter_1=int(profit_lst[0]),
        quarter_2=int(profit_lst[1]),
        quarter_3=int(profit_lst[2]),
        quarter_4=int(profit_lst[3])
    )
    # находим общую прибыль по каждому предприятию и записываем ее в словарь
    enterprise_profit[enterprise.name] = enterprise.quarter_1 + enterprise.quarter_2 + \
                                         enterprise.quarter_3 + enterprise.quarter_4

AVG = sum(enterprise_profit.values()) / N  # средняя прибыль в год для всех предприятий

more_avg = []
less_avg = []

for j in enterprise_profit:
    if enterprise_profit[j] >= AVG:
        more_avg.append(j)
    else:
        less_avg.append(j)

print(f'Средняя прибыль за год: {AVG}')
print(f'Предприятия, у которых прибыль выше средней: {more_avg}')
print(f'Предприятия, у которых прибыль ниже средней: {less_avg}')
