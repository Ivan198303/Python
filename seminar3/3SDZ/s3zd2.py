# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random
n = int(input("Введите число "))
list = []
list = [i for i in range(n)]
random.shuffle(list)
print(list)
if len(list) % 2 == 0:
    for i in range(len(list)//2):
        result = list[i]*list[len(list)-i-1]
        print(result)
else:
    for i in range(len(list)//2+1):
        result = list[i]*list[len(list)-i-1]
        print(result)
