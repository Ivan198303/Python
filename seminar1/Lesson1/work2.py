# 1. Напишите программу, которая будет на вход принимать число N и 
# выводить числа от -N до N   
#     Пример 
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# a = int(input("Введите число "))
# b = - a
# while b != a+1:
#     print(b)
#     b += 1

# print('Введите N: ')
# n = int(input())
# for i in range(-n,n+1):
#     print(i)

# a = abs(int(input()))
# print(list(range(-a,a+1)))
# 2. Напишите программу, которая будет принимать на вход дробь и показывать 
# первую цифру дробной части числа    
#     Пример  
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3for
# n = input()
# list_num = n.split(".")
# if len(list_num)>1:
#   print(list_num)
#   print(list_num[1][0])


# 3. Напишите программу, которая принимает на вход число и проверяет, кратно 
# ли оно 5 и 10 или 15, но не 30.
# n = int(input())
# if (n%5==0 and n%10==0 or n%15==0) and n%30!=0:
#   print("yes")
# else:
#   print("no")
