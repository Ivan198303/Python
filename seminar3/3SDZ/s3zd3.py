# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
from decimal import Decimal
result = [float(Decimal(i) / 100) for i in range(100, 115)]
random.shuffle(result)
print(result)
list = [round(i % 1, 2) for i in result if i % 1 != 0]
print(list)
print(max(list), min(list))
print(max(list) - min(list))

