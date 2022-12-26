# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
n = int(input("Введите число "))
list = []
list = [i for i in range(n)]
random.shuffle(list)
print(list)
num = 0
for i in range(0, len(list), 2):
    print((list[i]), end='  ')
    num = num + list[i]
print(f'Сумма чисел равна = {num}')
