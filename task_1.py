# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в
# диапазоне от 2 до 9. Примечание: 8 разных ответов.

multiples = {}

for i in range(2, 9):
    multiples[i] = len([num for num in range(2, 100) if num % i == 0])

print(multiples)

# 2
for i in range(2, 9):
    counter = 0
    for num in range(2, 100):
        if num % i == 0:
            counter += 1

    print(f'Кратных {i}: {counter}')
