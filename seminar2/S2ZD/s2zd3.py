# Задайте список из n чисел последовательности (1 + 1/n)^n
# и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06
n = int(input("Введите число "))
dict_num = {}
for i in range(1,n+1):
    dict_num[i] = round((1+1/i)**i,2)
print(dict_num)
print(sum(dict_num.values()))
