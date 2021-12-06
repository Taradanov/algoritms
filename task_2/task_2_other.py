# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)
def even_odd(a: int):
    a_list = [int(i) for i in str(a)]
    return sum([num%2==0 for num in a_list]), \
           sum([num%2==1 for num in a_list])

assert even_odd(123) == (1, 2)
assert even_odd(113) == (0, 3)
assert even_odd(2222) == (4, 0)