# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

def sum_1(num):
    sum = 0
    for i in range(num):
        sum += pow(-1, i) * (1 / pow(2, i))
    return sum


def sum_2_recursive(num):

    if num == 0:
        return 1

    return pow(-1, num) * (1 / pow(2, num)) + sum_2_recursive(num - 1)


def sum_2(num):
    # как то не удалось без обёртки))
    return sum_2_recursive(num - 1)

def sum_3(num):
    return sum([pow(-1, i) * (1 / pow(2, i)) for i in range(num)])



assert sum_1(5) == 0.6875
assert sum_1(7) == 0.671875
assert sum_1(9) == 0.66796875


assert sum_2(5) == 0.6875
assert sum_2(7) == 0.671875
assert sum_2(9) == 0.66796875

assert sum_3(5) == 0.6875
assert sum_3(7) == 0.671875
assert sum_3(9) == 0.66796875

