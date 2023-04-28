# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
a = int(input("Insert first number: "))
b = int(input("Insert second number: "))


def square(a, b):
    if b <1:
        return 1
    return a * square(a, b-1)


print(square(a, b))
