# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

import argparse

parser = argparse.ArgumentParser(description='(выработка в часах * ставка в час) + премия')
parser.add_argument('-hours', dest='hours', action="store", help='Выработка в часах', type=int)
parser.add_argument('-rate', dest='rate', action="store", help='Ставка в час', type=int)
parser.add_argument('-bonus', dest='bonus', action="store", help='Премия', type=int)

args = parser.parse_args()

print(f'Зарплата сотрудника {(args.hours * args.rate) + args.bonus}')
