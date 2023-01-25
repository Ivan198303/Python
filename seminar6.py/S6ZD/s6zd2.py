# 45. Найти сумму чисел списка стоящих на нечетной позиции
import random
n = int(input("Введите число "))
list = []
list = [random.randint(0, 100) for i in range(n)]
print(list)
result = sum([value for indx, value in enumerate(list) if indx % 2 == 1])
print(f'Сумма чисел равна = {result}')
b_nechet = sum(filter(lambda x: x if list.index(x) % 2 == 1 else False, list))
print(f'Сумма чисел равна = {b_nechet}')