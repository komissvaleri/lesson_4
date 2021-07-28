
isch_list = [i for i in range(100, 1001) if i % 2 == 0]
print(isch_list)

from functools import reduce
def func_1(i_p, i):
    return  i_p * i

print(reduce(func_1, isch_list))