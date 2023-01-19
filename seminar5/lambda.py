def summ(a, b):
    return a + b


print(summ(3, 5))


f = (lambda a, b: a + b if a > b else 0)  # это тожа самая функция но короче
print(f(2, 5))


def calc(op, a, b):
    print(op(a, b))


calc(lambda x, y: x + y, 4, 5)
