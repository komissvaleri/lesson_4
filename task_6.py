
def my_func_1():
    x = int(input('Введите число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(x), 10):
        print(i)
my_func_1()

def my_func_2():
    list = ["start", 1, "end", 2]

    from itertools import islice
    from itertools import cycle

    for i_1 in islice(cycle(list), 10):
        print(i_1)
my_func_2()


