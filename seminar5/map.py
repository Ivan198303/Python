a = [i for i in range(12)]
print(a)
a = list(map(lambda x: x + 10, a))  # увеличивает все элементы на 10
print(a)
a = list(map(lambda x: x + 10 if x > 6 else x + 0, a))  # увеличивает что > 6
print(a)
