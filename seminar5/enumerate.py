a = [1, 4, 9, 16, 25, 36, 49, 64]
for i in a:  # проходим по элементам списка
    print(i)
for i in range(len(a)):  # проходим по индексам списка
    print(i)
for indx, value in enumerate(a):  # проходим сразу по индексам и элементам.
    print(indx, value)
