# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random


def sort_array(arr):
    while True:

        was_reshuffle = False

        for i in range(1, len_arr):
            if arr[len_arr - i] > arr[len_arr - i - 1]:
                arr[len_arr - i], arr[len_arr - i - 1] = arr[len_arr - i - 1], arr[len_arr - i]
                was_reshuffle = True

        if not was_reshuffle:
            break


len_arr = 10000
arr_ = [random.randint(-100, 99) for i in range(len_arr)]
print(arr_)
sort_array(arr_)
print(arr_)
