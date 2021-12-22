# Библиотека с графикой, png прилагаются https://github.com/jmdana/memprof
from memprof import memprof

@memprof(plot = True)
def even_odd_1(a: int):
    a_list = [int(i) for i in str(a)]
    return sum([num % 2 == 0 for num in a_list]), sum([num % 2 == 1 for num in a_list])

@memprof(plot = True)
def even_odd_2(a):
    even = 0  # четные
    odd = 0
    while a > 0:
        last_num = a % 10
        a = a // 10
        if last_num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

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

@memprof(plot = True)
def even_odd_recursive_wrapped(a):
    even_odd_recursive(a)

# even_odd_1(2 ** 1_000_000) # По замеру 2.4 Мб
# even_odd_2(2 ** 1_000_000) # Менее 1
# even_odd_recursive_wrapped(2** 3_000) # Менее 1