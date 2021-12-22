from memory_profiler import profile

@profile
def even_odd_1(a: int):
    a_list = [int(i) for i in str(a)]
    return sum([num % 2 == 0 for num in a_list]), sum([num % 2 == 1 for num in a_list])

@profile
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

@profile
def even_odd_recursive_wrapped(a):
    even_odd_recursive(a)

# ***************************************************************************************
# even_odd_1(2 ** 3_000)
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#      3     38.7 MiB     38.7 MiB           1   @profile
#      4                                         def even_odd_1(a: int):
#      5     38.7 MiB      0.0 MiB         907       a_list = [int(i) for i in str(a)]
#      6     38.8 MiB      0.1 MiB        1813       return sum([num % 2 == 0 for num in a_list]), sum([num % 2 == 1 for num in a_list])

# ***************************************************************************************
# even_odd_2(2 ** 3_000)
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#      8     38.8 MiB     38.8 MiB           1   @profile
#      9                                         def even_odd_2(a):
#     10     38.8 MiB      0.0 MiB           1       even = 0  # четные
#     11     38.8 MiB      0.0 MiB           1       odd = 0
#     12     38.8 MiB      0.0 MiB         905       while a > 0:
#     13     38.8 MiB      0.0 MiB         904           last_num = a % 10
#     14     38.8 MiB      0.0 MiB         904           a = a // 10
#     15     38.8 MiB      0.0 MiB         904           if last_num % 2 == 0:
#     16     38.8 MiB      0.0 MiB         471               even += 1
#     17                                                 else:
#     18     38.8 MiB      0.0 MiB         433               odd += 1
#     19     38.8 MiB      0.0 MiB           1       return even, odd

# ***************************************************************************************
# Как то не информативно)
# even_odd_recursive_wrapped(2 ** 30)
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     35     38.6 MiB     38.6 MiB           1   @profile
#     36                                         def even_odd_recursive_wrapped(a):
#     37     38.6 MiB      0.0 MiB           1       even_odd_recursive(a)

# ***************************************************************************************
# even_odd_1(2 ** 1_000_000)
# Не понимаю минусовые цифры, но общая память показывает динамику: 43.5 - 39.0 MiB = 4.5
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#      3     39.0 MiB     39.0 MiB           1   @profile
#      4                                         def even_odd_1(a: int):
#      5     41.6 MiB -14635.7 MiB      301033       a_list = [int(i) for i in str(a)]
#      6     43.5 MiB -303773.7 MiB      602065       return sum([num % 2 == 0 for num in a_list]), sum([num % 2 == 1 for num in a_list])

# ***************************************************************************************
# even_odd_2(2 ** 1_000_000)
# По памяти меньше но скорость в 20 раз медленнее. ~1.5mb

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#      8     39.1 MiB     39.1 MiB           1   @profile
#      9                                         def even_odd_2(a):
#     10     39.1 MiB      0.0 MiB           1       even = 0  # четные
#     11     39.1 MiB      0.0 MiB           1       odd = 0
#     12     40.5 MiB  -9408.3 MiB      301031       while a > 0:
#     13     40.5 MiB  -9407.5 MiB      301030           last_num = a % 10
#     14     40.5 MiB  -9407.6 MiB      301030           a = a // 10
#     15     40.5 MiB  -9408.3 MiB      301030           if last_num % 2 == 0:
#     16     40.5 MiB  -4705.4 MiB      150462               even += 1
#     17                                                 else:
#     18     40.5 MiB  -4702.9 MiB      150568               odd += 1
#     19     40.5 MiB      0.0 MiB           1       return even, odd