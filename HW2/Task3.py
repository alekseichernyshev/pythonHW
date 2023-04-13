# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число'))
result = []
for i in range(0, n):
    if 2**i <= n:
        result.append(2**i)
print(result)