# Найдите сумму цифр трехзначного числа.

n = int(input('Введите трёхзначное число: '))
if n < 100 or n > 999:
    print('Нужно ввести трёхзначное число')
else:
    print(n // 100 + n // 10 % 10 + n % 10)