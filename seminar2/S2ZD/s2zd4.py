# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.
import random
n = int(input("Введите число "))
list = []
list = [i for i in range(-n, n+1)]
print(list)
data = open('file.txt', 'w')
data.writelines(str(list))
data.close()
random.shuffle(list)
print(list)