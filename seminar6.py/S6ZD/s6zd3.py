# 46. Найти произведение пар чисел списка
# (парой считаем первый и последний, второй предпоследний и тд)
import random
a = int(input('Введите число '))
list = []
list = [random.randint(0, 10) for i in range(a)]
print(list)
if len(list) % 2 == 0:
    result = [list[indx]*list[-indx-1] for indx, value in enumerate(range(len(list)//2))]
    print(result)
else:
    result = [list[indx]*list[-indx-1] for indx, value in enumerate(range(len(list)//2+1))]
    print(result)