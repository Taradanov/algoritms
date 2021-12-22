#
# В ДЗ к 4 уроку я оценивал быстродействие четырех алгоритмов расчета чисел Фибоначчи, победил алгоритм
# eratosthenes_1. Сегодня я буду оценивать потребление памяти
from memprof import memprof


# **************************************************************************************
# Вариант № 1
# Функция возвращает список ("решето"), в котором все составные числа заменены нулями:
# @profile
@memprof(plot=True)
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
@memprof(plot=True)
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
@memprof(threshold=1024, plot=True)
def eratosthenes_3(n):
    s = [x for x in range(2, n + 1) if
         x not in [i for sub in [list(range(2 * j, n + 1, j)) for j in range(2, n // 2)] for i in sub]]
    return s


# **************************************************************************************
# Вариант №4
@memprof(threshold=1024, plot=True)
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


# eratosthenes_1(10_000_000)  # 76mb
# eratosthenes_2(10_000_000)  # 76mb
# eratosthenes_3(5_000) # Не более 350 кб, график получился интересный и потребление памяти минимальное, а алгоритм очень медленный
# eratosthenes_4(100_000) # Забавный график расширения списка)) очень медленно
