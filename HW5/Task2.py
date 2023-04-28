# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input("Insert first number: "))
b = int(input("Insert second number: "))


def sum(a, b):
    if b == 0:
        return a
    return sum(a +1, b - 1)

print(sum(a, b))
