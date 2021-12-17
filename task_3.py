# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.  Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием
# также недопустима).
import random
import statistics
import time


# Источник https://ru.stackoverflow.com/questions/897278/%D0%94%D0%B5%D0%BA%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80-%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B9-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D0%B8%D1%82-%D0%B2%D1%80%D0%B5%D0%BC%D1%8F-%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8
def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(round((time.perf_counter_ns() - start_time) / 10 ** 9, 3))
        return res

    return wrapped


@time_of_function
def get_mediana(arr_):
    # Дистанция - разница между расстояниями до обоих концов
    max_distance = len(arr_)
    # Выбрал все уникальные значения
    values = set(arr_)

    mediana = None
    for i in values:
        # Посчитаю количество элементов больше и меньше медианы
        distance_for_current_value = abs(len([num for num in arr_ if num > i]) - len([num for num in arr_ if num < i]))

        if distance_for_current_value < max_distance:
            max_distance = distance_for_current_value
            mediana = i

        if distance_for_current_value == 0:
            return mediana

    # return 100
    return mediana


@time_of_function
def get_mediana_from_statistics(arr_):
    return statistics.median(arr)


m = 2000000
# Создал список
arr = [random.randint(10, 100) for i in range(m * 2 + 1)]

assert get_mediana_from_statistics(arr) == get_mediana(arr)
# Разница на два порядка))) Не быстро.
# 0.506
# 36.499
