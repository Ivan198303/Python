num = [1, 2, 3, 4, 5, 6]
months = ["июнь", "июль", "июль2", "июль3", "июль4", "июль5"]
a = list(zip(num, months))  # объединяет два списка в один по самому мин,в
# Кортежи  Для того чтобы это стало списком нужно вначале прописывать "list"
print(a)
print(a[1])  # так мы обращаемся к кортежу полностью
print(a[3][0])  # так мы обращаемся к первой части кортежа, указывается индекс
print(a[3][1])  # так мы обращаемся ко второй части кортежа, указывается индекс
