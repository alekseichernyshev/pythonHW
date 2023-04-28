# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
def fillSet(number):
    res = list(map(int, input("Insert set: ").split()))
    result = res[0: number]
    return result


n = int(input("Insert first number: "))
m = int(input("Insert second number: "))
list1 = fillSet(n)
list2 = fillSet(m)
helper = set()
for x in list1:
    helper.add(x)
for x in list2:
    helper.add(x)
result = list(helper)
result.sort()

print(result)
