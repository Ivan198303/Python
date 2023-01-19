a = [i for i in range(1, 9)]  # создание списков через list comprehension
print(a)
a = []
for i in range(1, 9):  # создание списка стардартным путем
    a.append(i)
print(a)
f = a
f = [i for i in range(1, 9) if i % 2 == 0]  # добавили условие
print(f)
f = [(i, i+1) for i in range(1, 9) if i % 2 == 0]  # сделали кортеж
print(f)


def g(x):
    return x**2


f = [g(i) for i in range(1, 9) if i % 2 == 0]  # добавили функцию
print(f)
f = [(i, g(i)) for i in range(1, 9) if i % 2 == 0]  # добавили функцию и кортеж
print(f)
k = [1, 2, 3, 5, 8, 15, 23, 38]
k = [(i, g(i)) for i in k if i % 2 == 0]
print(k)
