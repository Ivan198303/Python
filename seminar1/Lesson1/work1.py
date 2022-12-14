# num_1 = int(input("Введите первое число "))
# num_2 = int(input("Введите второе число "))
# if num_2 == num_1 ** 2:
#     print('Число num_1 является квадратом числа num_2 ')
# elif num_1 == num_2 ** 2:
#     print('Число num_2 является квадратом числа num_1 ')
# print('Числа не является квадратом друг друга')
# #Напишите программу, которая принимает на вход два числа и проверяет
# , является ли одно число квадратом другого.
# a = int(input())
# b = int(input())
# if a**2==b or b**2==a:
#   print("yes")
# else:
#   print("no")
# Напишите программу, которая на вход принимает 5 чисел
#  и находит максимальное. из них.
# a = int(input())
# max = a
# for i in range(5):
#   a = int(input())
#   if a>max:
#     max = a
# print(max)
# a = input()
# list_num = a.split(",")
# print(max(list_num))
a = input()
list_num = list(map(int, a.split(" ")))
print(list_num)
