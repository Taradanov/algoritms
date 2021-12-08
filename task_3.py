# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

arr = [random.randint(-100, 100) for i in range(10)]
print(arr)

min_int = arr[0]
max_int = arr[0]

for i in range(len(arr)):
    if arr[i] > max_int:
        max_int = arr[i]
        max_index = i
    if arr[i] < min_int:
        min_int = arr[i]
        min_index = i

arr[max_index], arr[min_index] = arr[min_index], arr[max_index]

print(arr)

print('max_int', max_int, 'min_int', min_int, 'max_index', max_index, 'min_index', min_index)
