#Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.
from typing import List

start = int(input("Insert start position: "))
step = int(input("Insert step: "))
count = int(input("Insert count of numbers: "))
helper = start
result = list()
while count > 0:
    result.append(start)
    start += step
    count -= 1
print(result)

for i in range(count):
    print(start + i * step)
