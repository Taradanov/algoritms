# Взял задачу:

# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

# Я хочу выяснить, какая из двух функций быстрее even_odd_1 или even_odd_2
# в even_odd_1 обход списка выполняется 2 раза и есть преобразование типов, должно быть медленнее
# even_odd_recursive в качестве тренировки

# import timeit
import cProfile


def test():
    assert even_odd_recursive(123) == (1, 2)
    assert even_odd_recursive(113) == (0, 3)
    assert even_odd_recursive(2222) == (4, 0)

    assert even_odd_1(123) == (1, 2)
    assert even_odd_1(113) == (0, 3)
    assert even_odd_1(2222) == (4, 0)

    assert even_odd_2(123) == (1, 2)
    assert even_odd_2(113) == (0, 3)
    assert even_odd_2(2222) == (4, 0)

    assert even_odd_1(2**100_000) == even_odd_2(2**100_000)



def even_odd_1(a: int):
    a_list = [int(i) for i in str(a)]
    return sum([num % 2 == 0 for num in a_list]), sum([num % 2 == 1 for num in a_list])


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

# test()
# print(even_odd_1(2**1_000_000))

# # *** Следующие три настройки не интересны, так как рекурсия заваливается и не видно ответа на вопрос
# cProfile.run('even_odd_1(2**3_000)')
# # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# #         1    0.000    0.000    0.000    0.000 task_1.py:28(even_odd_1)
#
# cProfile.run('even_odd_2(2**3_000)')
# # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# #         1    0.001    0.001    0.001    0.001 task_1.py:32(even_odd_2)
#
# cProfile.run('even_odd_recursive(2**3_000)')
# # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# #     905/1    0.002    0.000    0.002    0.002 task_1.py:44(even_odd_recursive)

# # *** Следующие два замера для большого числа 2**1_000_000
# cProfile.run('even_odd_1(2**1_000_000)')
# # 8 function calls in 1.863 seconds
# # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# #         1    0.004    0.004    1.887    1.887 <string>:1(<module>)
# #         1    1.775    1.775    1.883    1.883 task_1.py:28(even_odd_1)
#
# cProfile.run('even_odd_2(2**1_000_000)')
# # 4 function calls in 40.089 seconds
# # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# #         1   40.085   40.085   40.085   40.085 task_1.py:33(even_odd_2)

# #***
# Оценка timeit
# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 1000 -s "import task_1_1" "task_1_1.even_odd_1(2**3_000)"
# 1000 loops, best of 5: 269 usec per loop

# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 1000 -s "import task_1_1" "task_1_1.even_odd_2(2**3_000)"
# 1000 loops, best of 5: 512 usec per loop

# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 1000 -s "import task_1_1" "task_1_1.even_odd_recursive(2**3_000)"
# 1000 loops, best of 5: 649 usec per loop

# #***
# Второй замер
# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 1000 -s "import task_1_1" "task_1_1.even_odd_1(2**30_000)"
# 1000 loops, best of 5: 3.95 msec per loop
# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 1000 -s "import task_1_1" "task_1_1.even_odd_2(2**30_000)"
# 1000 loops, best of 5: 39.8 msec per loop

# #***
# 1. Рекурсия ограничена стеком, для такой задачи применять рекурсию можно только в целях написания рекурсию
# 2. Для меня стало неожиданным то, что преобразование числа в строку плюс формирование двух списков плюс суммирование элементов списков
#     выполняется быстрее чем обход списка. Я ожидал примерно двухкратного расхождения, а получил на большом числе десятикратное


# #***
# и вишенка на торт:

# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 10 -s "import task_1_1" "task_1_1.even_odd_1(2**1000000)"
# 10 loops, best of 5: 1.79 sec per loop
# PS C:\Users\Taradanov.NV\PycharmProjects\algoritms\task_1_1> python -m timeit -n 10 -s "import task_1_1" "task_1_1.even_odd_2(2**1000000)"
# 10 loops, best of 5: 40.5 sec per loop

# #***
# что соотносится с измерениями timeit