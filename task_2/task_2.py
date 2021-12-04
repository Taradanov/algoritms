# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

def even_odd(a):
    even = 0  # четные
    odd = 0
    while a > 0:
        last_num = a % 10
        a = a // 10
        if last_num % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f'Количество чётных: {even}, нечетных: {odd}')


def even_odd_recursive(a):
    if a == 0:
        return 0, 0

    last_num = a % 10
    even, odd = even_odd_recursive(a // 10)

    if last_num % 2 == 0:
        even += 1
    else:
        odd += 1
    return even, odd

a = int(input('Введите число: '))
even_odd(a)

even, odd = even_odd_recursive(a)
print(f'Количество чётных: {even}, нечетных: {odd}')
