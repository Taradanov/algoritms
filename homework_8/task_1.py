# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

# Каюсь, грешен, частично списал)))

import hashlib

string = input('Введите строку, состоящую только из маленьких латинских букв: ')

assert string.lower() == string

substrings = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        substrings.add(hash_str)

print(f'{len(substrings)-1} различных подстрок в строке {string}')
