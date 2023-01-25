# a = [34, 12, 567, 657]
# r = sorted(a)  # сортировка по возрастанию
# print(r)
# r = sorted(a, reverse=True)  # сортировка по убыванию
# print(r)

# b = [12, 34, 567, 657, 15, 2]  # сортироовка по четности


# def sorting(x):
#     if x % 2 == 0:
#         return True
#     return (x)


# c = sorted(b, key=sorting)  
# print(c)

# b = ['ffdsf', 'dsd', 'd', 'aaa']  # сортироовка по длинне
# r = sorted(b, key=len)
# print(r)

# b = ['ffdsf', 'bsd', 'd', 'aaa']  # сортироовка по первой букве
# r = sorted(b, key=lambda x: x[0])
# print(r)

# a = {4: 'as', 2: 'bd', 3: 've'}  # сортировка по ключам (4.2.3)
# r = sorted(a)
# print(r)

a = [(2, 5, 3), (7, 4, 3), (1, 9, 5)]  # сортировка кортежей по ключам  (5.4.9)
r = sorted(a, key=lambda x: x[1])
print(r)