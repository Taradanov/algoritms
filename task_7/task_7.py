# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или
# равносторонним

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Такого треугольника не существует')
elif a == b == c:
    print('Треугольник равносторонний')
elif a == b or b == c or c == a:
    print('Это равнобедренный треугольник')
else:
    print('Это разносторонний треугольник')
