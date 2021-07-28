
# def fact(n):
#     x = 1
#     for el in range(1, n + 1):
#         x *= el
#         yield x
#
# n = int(input('Введите число, факториал которого нужно вычислить: '))
# for el in fact(n):
#     print(el)

from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)
gen = fact()
n = 0
for el in gen:
    if n < 4:
        print(el)
        n += 1
    else:
        break


