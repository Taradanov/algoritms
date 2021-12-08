# Определить, какое число в массиве встречается чаще всего.

import random

arr = [random.randint(0, 9) for i in range(100)]
counter ={}
for elem in arr:
    if counter.get(elem) ==None:
        counter[elem] = 1
    else:
        counter[elem] += 1

print(counter)

max = 0
index = 0

for key, value in counter.items():
    if value > max:
        index = key
        max = value
print(f'число {index} количество {max}')
