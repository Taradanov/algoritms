a = int(input())
b = int(input())

if a % b == 0:
    print(f'Число a={a} делиться на число b={b}')

else:
    print(f'Число a={a} НЕ делиться на число b={b}')
    print(f'остаток числа = {a%b}')

print(f'Частное {a//b}')

