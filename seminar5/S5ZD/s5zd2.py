# 40. Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек,
# далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных,
#  получить строку входных данных.
import itertools
num = "111112222334445"
letters = "AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE"
num_1 = (list(map(int, num)))
letters_1 = (list(map(str, letters)))
print(letters_1)
for item, group in itertools.groupby(letters_1):
    print(f'{len(list(group))}{item}', end='')
print()
print(num_1)
for item, group in itertools.groupby(num_1):
    print(f'{len(list(group))}{item}', end='')
print()
res = '6A1F2D7C1A17E'
number = (list(map(str, res)))
print(number)