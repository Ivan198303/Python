import random
# напините программу на python для поиска пересечения двух заданных
# массивов с
# помощью lambda
# [1, 2, 3, 5, 7 ,8 ,9 10]
# [1, 2, 4, 8 ,9]
a = [1, 2, 3, 5, 7, 8, 9, 10]
b = [1, 2, 4, 8, 9]
res = list(filter(lambda i: i in b, a))
print(res)

# Сделать с помощью filter и lambda
# напишите программу, удаляющую из текста все слова, содержащие "абв"
# вывести все пробелы и их индексы
text_1 = 'абвгн прог абвгж рама авб'
text = text_1.split()
result = list(filter(lambda x: not "абв" in x.lower(), text))
print(result)
for indx, value in enumerate(text_1):  # проходим сразу по индексам и элементам
    if value == " ":
        print(indx)

# имеется упорядоченный список
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Перебрать все элементы этого списка с помощью функции enumerate и
# элементы на главной диагонали превратить в нули
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for indx, value in enumerate(a):
#     print(indx, value)
#     value[indx] = 0
for indx, value in enumerate(a):
    for indx_2, value_2 in enumerate(a):
        if indx == indx_2:
            value[indx_2] = 0
print(a)


# имеется список id сотрудников из 5 элементов, id - случайное число
# от 1 до 100
# Имеется список сотрудников из 5 элементов
# Сопоставить имена с id
# вывести имена сотрудников с нечетным id

id = [random.randint(1, 100) for i in range(5)]
name = ["Вова", "Вася", "Витя", "Ваня", "Вася1"]
print(id)
res_list = list(zip(id, name))
print(res_list)
res_list2 = list(filter(lambda x: x[0] % 2 == 1, res_list))
print(res_list2)
