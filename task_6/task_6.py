# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
from builtins import chr

# a - 97, z-122/
# print(chr(97))

a = int(input('Введите число a: '))

if a < 1 or a > 26:
    print(f'Ошибка, число {a} введено неверно')
else:
    symbol = chr(96 + a)
    print(f'Это буква {symbol}')
