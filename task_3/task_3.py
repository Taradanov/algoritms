# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.
import result as result


def reverse_1(a: int) -> int:
    reverse_a = 0
    while a > 0:
        number = a % 10
        reverse_a = reverse_a * 10 + number
        a = a // 10
    return reverse_a


def reverse_2(a, b=0):
    if a < 10:
        return b * 10 + a

    return reverse_2(a // 10, b * 10 + a % 10)


def reverse_3(a: int):
    str_ = ''
    for s in str(a):
        str_ = f'{s}{str_}'
    return int(str_)


assert reverse_1(102) == 201
assert reverse_1(100) == 1
assert reverse_1(3486) == 6843

assert reverse_2(102) == 201
assert reverse_2(100) == 1
assert reverse_2(3486) == 6843

assert reverse_3(102) == 201
assert reverse_3(100) == 1
assert reverse_3(3486) == 6843
