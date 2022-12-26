# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
import random
n = int(input("Введите кол-во элементов в списке "))
list = []
list = [random.randint(0, 100) for i in range(n)]
list.append(45)
list.append(0)
print(list)
for i in list:
    c = i
    b = ''
    if i != 0 and i != 1:
        while i > 0:
            y = str(i % 2)
            b = y + b
            i = int(i / 2)
        print(f"для числа {c} двоичная кодировка {b}")
