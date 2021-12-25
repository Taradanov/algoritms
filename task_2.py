# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


# Каюсь, грешен, списал
import random


def sort_array(arr):
    if len(arr) < 2:
        return arr
    left = sort_array(arr[:len(arr) // 2])
    right = sort_array(arr[len(arr) // 2:])
    i = j = 0
    result = []
    while len(left) > i or len(right) > j:
        if len(left) <= i:
            result.append(right[j])
            j += 1
        elif len(right) <= j:
            result.append(left[i])
            i += 1
        elif right[j] > left[i]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
    return result


# Генерация массива [0, 50)
def generate_arr(len_arr):
    arr = []
    while True:

        if len(arr) == len_arr:
            break

        number = random.random() * 50
        if number == 50.0:
            continue

        arr.append(number)

    return arr


arr_ = generate_arr(10)

print(arr_)
arr_ = sort_array(arr_)
print(arr_)
