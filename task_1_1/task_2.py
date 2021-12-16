# Все функции взяты с https://ru.wikibooks.org/wiki/%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8_%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%BE%D0%B2/%D0%A0%D0%B5%D1%88%D0%B5%D1%82%D0%BE_%D0%AD%D1%80%D0%B0%D1%82%D0%BE%D1%81%D1%84%D0%B5%D0%BD%D0%B0
# Для меня это задание про "поковырять профайлер" чем про написать алгоритм

# Источник: https://habr.com/ru/company/vk/blog/201594/
# Не совсем понимаю как работают декораторы, надеюсь это применение поможет разобраться
import cProfile
import timeit

# Повозился с декоратором - не получилось, не смог открыть файл pof
def profile(func):
    """Decorator for run function profile"""

    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        # profiler.print_stats()
        profiler.dump_stats(profile_filename)
        return result

    return wrapper


# **************************************************************************************
# Вариант № 1
# Функция возвращает список ("решето"), в котором все составные числа заменены нулями:
# @profile
def eratosthenes_1(n):  # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0  # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return [x for x in sieve if x != 0]


# **************************************************************************************
# Вариант № 2
def eratosthenes_2(n):  # число, до которого хотим найти простые числа
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n + 1, number):
                numbers[candidate - 2] = 0
    return list(filter(lambda x: x != 0, numbers))  # выводим простые числа


# **************************************************************************************
# Вариант № 3 (списковое включение)
# Полностью построено на генераторах списков.
def eratosthenes_3(n):
    s = [x for x in range(2, n + 1) if
         x not in [i for sub in [list(range(2 * j, n + 1, j)) for j in range(2, n // 2)] for i in sub]]
    return s


# **************************************************************************************
# Вариант №4
def eratosthenes_4(n):
    a = True
    s = []
    for x in range(2, n):
        for y in range(2, n):
            if x != y and y != 1:
                if not x % y:
                    a = False
                    break
        if a == True:
            s.append(x)
        a = True
    return s

def test():
    assert eratosthenes_1(100) == eratosthenes_2(100) == eratosthenes_3(100) \
           == eratosthenes_4(100)


# test()

#************************************************************************************************************************************
# Начнем с замера  timeit
# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 100 -s "import task_2" "task_2.eratosthenes_1(100)"
# 100 loops, best of 5: 16.7 usec per loop
# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 100 -s "import task_2" "task_2.eratosthenes_2(100)"
# 100 loops, best of 5: 23.7 usec per loop
# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 100 -s "import task_2" "task_2.eratosthenes_3(100)"
# 100 loops, best of 5: 2.7 msec per loop
# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 100 -s "import task_2" "task_2.eratosthenes_4(100)"
# 100 loops, best of 5: 186 usec per loop
# Решение №3 оказалось медленнее на два порядка

# *************************************************************************************
# Выбрал для расчета n = 10_000

# cProfile.run('eratosthenes_3(10_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   70.816   70.816 task_2.py:50(eratosthenes_3)
# C такой задержкой алгоритм 3 выбывает из соревнования


# cProfile.run('eratosthenes_1(100_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.027    0.027    0.031    0.031 task_2.py:26(eratosthenes_1)
#
# cProfile.run('eratosthenes_2(100_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.065    0.065    0.076    0.076 task_2.py:38(eratosthenes_2)

# cProfile.run('eratosthenes_4(100_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1   81.093   81.093   81.099   81.099 task_2.py:58(eratosthenes_4)
# И 4 алгоритм выбыл

# cProfile.run('eratosthenes_1(1_000_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.300    0.300    0.334    0.334 task_2.py:26(eratosthenes_1)

# cProfile.run('eratosthenes_2(1_000_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.526    0.526    0.619    0.619 task_2.py:38(eratosthenes_2)

# cProfile.run('eratosthenes_1(10_000_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    3.549    3.549    3.923    3.923 task_2.py:26(eratosthenes_1)

# cProfile.run('eratosthenes_2(10_000_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    5.739    5.739    6.659    6.659 task_2.py:38(eratosthenes_2)

# cProfile.run('eratosthenes_1(100_000_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1   38.270   38.270   41.550   41.550 task_2.py:26(eratosthenes_1)

# cProfile.run('eratosthenes_2(100_000_000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1   55.990   55.990   65.113   65.113 task_2.py:38(eratosthenes_2)


# Победила реализация eratosthenes_1

