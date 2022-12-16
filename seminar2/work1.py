# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Каждый член последовательности больше предыдущего в 3 раза, знаки у элементов чередуются.
# *Пример:*
n = int(input("Введите число: "))
m = 1
for i in range(1,n+1):
    print(m, end = " ")
    m*=-3

        # n = int(input())
        # symbol = 1
        # print(symbol, end = " ")
        # n = int(input())
        # symbol = 1
        # for i in range(n):
        #     print(symbol, end=" ")
            #     symbol *= -3
            # for i in range(n-1):
            #     symbol *= -3
            #     print(symbol, end = " ")
# - Для N = 5: 1, -3, 9, -27, 81

# 13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# Пример:
# Строка - "dabccabccabcc"
# Подстрока - "ab"
# Количество вхождений - 2
# Данная программа должна вывести n рядов, заполненных знаком ‘*’ определенным образом. А именно: в первом ряду должно быть n «звездочек», в втором n-1, и так далее. А в последнем ряду таким образом будет одна «звездочка». Причем убывать эти «звездочки» должны справа налево. Число n вводится пользователем.
# Введите количество рядов: 5
# *****
# ****
# ***
    # num = int(input("Введите число: "))
    # for i in range(num,0,-1):
    #     for j in range(0,i):
    #         print("*",end="")
    #     print()

# n = int(input())
# for i in range(n,0,-1):
#     print("*"*i)


#     13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# Пример:
# Строка - "dabccabccabcc"
# Подстрока - "ab"
# Количество вхождений - 3
    # stroka = input("Введите Строку: ")
    # podstroka = input("Введите подстроку: ")

    # if podstroka not in stroka:
    #     print("Данной строки нет")
    # else:
    #     sum = 0
    #     for i in range(0,len(stroka)-len(podstroka)+1):
    #         if podstroka in stroka[i:i+len(podstroka)]:  
    #             sum+=1
    #     print(sum)
# line = input()
# sub_line = input()
# print(line.count(sub_line))
    # line = input()
    # sub_line = input()

    # count = 0

    # for i in range(0,len(line)-len(sub_line)+1):
    #     if line[i:i+len(sub_line)] == sub_line:
    #         count+=1
    # print(count)
