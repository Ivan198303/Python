a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def chek_num(x):
    if x % 2 == 0:
        return True


a_chet = list(filter(chek_num, a))
print(a_chet)
b_chet = list(filter(lambda x: True if x % 2 == 0 else False, a))
# (not x%2 == 0, a))#
print(b_chet)
