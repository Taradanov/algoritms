# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# Первая часть из задачи 3
import random
def summary(arr):

    min_int = arr[0]
    max_int = arr[0]

    min_index = 0
    max_index = 0

    for i in range(len(arr)):
        if arr[i] > max_int:
            max_int = arr[i]
            max_index = i
        if arr[i] < min_int:
            min_int = arr[i]
            min_index = i

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    sum = 0

    print(arr)

    for elem in arr[min_index+1:max_index]:
        sum += elem
    print(arr)
    print(min_index, max_index)
    print(sum)


summary([random.randint(-100, 100) for i in range(10)])
