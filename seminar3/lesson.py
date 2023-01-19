# # Решение с семинара 1 вариант
# def dec_to_bin(num. result= ""):
#     if num == 0:
#         return result [::-1]
#     result += str(num % 2)
#     return dec_to_bin(num//2.result)
# print(dec_to_bin(int(input())))
# # Решение с семинара 2 вариант
# print(bin(int(input()))[2::])
#Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# import datetime
# import time
# # def random_int(num):
# #     rand = datetime.datetime.now().microsecond%num
# #     return rand+1
#
# for i in range(10):
#     time.sleep(0.01)
#     print(datetime.datetime.now().microsecond)

# #Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# a = ["sr","ere","12","wewe"]
# n = int(input())
# for i in a:
#     if i.isdigit() and int(i) == n:
#         print(a.index(i))
# n = int(input())
# if n in a:
#     print(a.index(n))
# else:
#     print(-1)

#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# list_str = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# sub_str = "йцу"
# count=0
# for i in range(len(list_str)):
#     if list_str[i] == sub_str:
#         count += 1
#     if count == 2:
#         print(i)
#         break
# else:
#     print(-1)
