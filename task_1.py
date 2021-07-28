
# from sys import argv
# name_script, hours_1, sum_hour, prem_1 = (1, 2, 3, 4)
#
# print('Имя скрипта: ', name_script)
# print("\n <<Расчет ЗП сотрудника>>")
# print('Количество отработанных часов: ', hours_1)
# print('Часовая оплата: ', sum_hour)
# print('Премия: ', prem_1)
# print('ЗП сотрудника: ', (float(hours_1) * float(sum_hour)) + float(prem_1))

def zp_calc():
    hours = float(input('Введите количество отработанных часов: '))
    sum_hour = float(input('Введите сумму оплаты работы за 1 час: '))
    prem = float(input('Введите размер премии: '))
    x = hours * sum_hour + prem
    return x

print(f'Расчет зарабатной платы: {zp_calc()}')