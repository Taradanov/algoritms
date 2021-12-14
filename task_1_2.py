# В ДЗ к 4 уроку я оценивал быстродействие трех алгоритмов количества четных и нечетных цифр в числе
# Произведу оценку потребления памяти

# https://code.tutsplus.com/ru/tutorials/understand-how-much-memory-your-python-objects-use--cms-25609
# Источник: https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python

import sys
from numbers import Number
from collections import deque
from collections.abc import Set, Mapping

ZERO_DEPTH_BASES = (str, bytes, Number, range, bytearray)


def getsize(obj_0):
    """Recursively iterate to sum size of object & members."""
    _seen_ids = set()

    def inner(obj):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size = sys.getsizeof(obj)
        if isinstance(obj, ZERO_DEPTH_BASES):
            pass  # bypass remaining control flow and return
        elif isinstance(obj, (tuple, list, Set, deque)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, Mapping) or hasattr(obj, 'items'):
            size += sum(inner(k) + inner(v) for k, v in getattr(obj, 'items')())
        # Check for custom object instances - may subclass above too
        if hasattr(obj, '__dict__'):
            size += inner(vars(obj))
        if hasattr(obj, '__slots__'):  # can have __slots__ with __dict__
            size += sum(inner(getattr(obj, s)) for s in obj.__slots__ if hasattr(obj, s))
        return size

    return inner(obj_0)


def even_odd_1(a: int):
    used_memory = 0
    used_memory += getsize(a)

    numbers_list = [int(i) for i in str(a)]
    used_memory += getsize(numbers_list)

    even = [num % 2 == 0 for num in numbers_list]
    used_memory += getsize(even, )

    odd = [num % 2 == 1 for num in numbers_list]
    used_memory += getsize(odd)

    sum_even = sum(even)
    sum_odd = sum(odd)

    used_memory += getsize(sum_even)
    used_memory += getsize(sum_even)

    print(used_memory)

    return sum_even, sum_odd


# Замер памяти: 23932

def even_odd_2(a):
    used_memory = 0
    used_memory += getsize(a)

    even = 0  # четные
    odd = 0

    while a > 0:
        last_num = a % 10
        a = a // 10
        used_memory += getsize(a)
        if last_num % 2 == 0:
            even += 1
        else:
            odd += 1

    used_memory += getsize(even)
    used_memory += getsize(odd)
    print(used_memory)

    return even, odd


def even_odd_recursive(a):
    if a == 0:
        return 0, 0, 0

    last_num = a % 10
    even, odd, used_memory = even_odd_recursive(a // 10)
    used_memory += getsize(a)
    if last_num % 2 == 0:
        even += 1
    else:
        odd += 1
    used_memory += getsize(even)
    used_memory += getsize(odd)

    return even, odd, used_memory


# len(str(2**3000)) == 904, стек не переполнится

even_odd_1(2 ** 3_000)
# Замер памяти: 24360

even_odd_2(2 ** 3_000)
# Замер памяти: 204408, я так понимаю, это из-за неизменяемости int и большого количества операции деления

even, odd, used_memory = even_odd_recursive(2 ** 3_000)
print(used_memory)
# Замер памяти: 254948

# Теперь замеры на большом числе
even_odd_1(2**100000)  # 753260
even_odd_1(2**100000)  # 753260


# Теперь попробуем с декоратором см. task_1_3
