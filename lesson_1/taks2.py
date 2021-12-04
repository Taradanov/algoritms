x = int(input())


if x > 0:
    y = x * 2 - 10
elif x < 0:
    y = abs(x) * 2 - 1
else:
    y = 0

print(y)