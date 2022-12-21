none = input(" Как вас зовут")
print("Привет ", none)

num_1 = int(input("Введите первое число "))
num_2 = int(input("Введите второе число "))
res = num_1 + num_2
print("Результат вычесления ", res)

num = int(input("Введите первое число "))
if num >= 100:
    print("true")
elif num <= 50:
    print("true")
else:
    print("false")

# i = 0
# while i<10:
#     print (i, end = ', ')
#     i+=1
# for j in 'hello':
#     if j =='d':
#         break
#     print (j*2, end = ', ')
# else:
#     print ("Нет буквы d")

# l=[]
# l.append (23) # добавление элемента в массив
# b=[23, 43]
# l.extend (b) # добавление в массив элементов другого массива
# l.insert (1,56) # добавление элемента с указаным индексом (индекс, добавляет)
# l.remove () # удаляет указанный элемент один раз
# l.pop() # (удаляет элемент с указанным индексом, если ни чего
# не указывать убирает последний
# l.index ()# находит элемент и выводит его индекс
# l.count ()# находит количество указанных элементов в списке
# l.sort ()# сортирует список
# l.reverse # переворачивает список
    # перевод из строки на цифры
    # a = "23.567"
    # list_num = a.split(".")
    # print(list_num)
    # for i in range(len(list_num)):
    #     list_num[i] = int(list_num[i])
    # print(list_num)
        # a = "23.567"
        # list_num = a.split(".")
        # list_num=list(map(int,list_num))
        # print(list_num)
