# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minNum = int(input("Insert minimal number: "))
maxNum = int(input("Insert maximal number: "))
result = list()
for i in range(len(array)):
    if minNum <= array[i] <= maxNum:
        result.append(i)
print(result)
