# **44. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
# print("Введите координаты точек")
# x = int(input('Введите координату 1 точки по оси Х '))
# y = int(input('Введите координату 1 точки по оси Y '))
# x1 = int(input('Введите кординату 2 точки по оси X '))
# y1 = int(input('Введите кординату 2 точки по оси Y '))
# distance = ((x-x1)**2+(y-y1)**2)**0.5
# print(distance)
print("Введите координаты точек А и B")
A = [int(input(f"Введите {i} кординаты точки А ")) for i in 'xy']
B = [int(input(f"Введите {i} кординаты точки B ")) for i in 'xy']
distance = round((sum([(x[1]-x[0])**2 for x in zip(A, B)])**0.5), 3)
print(distance)