# # Решение с семинара 1 вариант
# def dec_to_bin(num. result= ""):
#     if num == 0:
#         return result [::-1]
#     result += str(num % 2)
#     return dec_to_bin(num//2.result)
# print(dec_to_bin(int(input())))
# # Решение с семинара 2 вариант
# print(bin(int(input()))[2::])