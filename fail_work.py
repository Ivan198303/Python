# рандомный перемешивание списка из чисел
import datetime
def random_int(num):
    rand = datetime.datetime.now().microsecond/10**6
    return int(num*rand)

a = [1 , 2, 3, 4, 5, 6]
print(a)
random_int(5)
for i in range(len(a)-1,-1,-1):
    j = random_int(i+1)
    a[i],a[j] = a[j],a[i]
print(a)
# рандомный список 
import random
a = [random.randint(-100, 100) for x in range(random.randint(0, 100))]

# рандомный список 
import random
n = int(input("Введите число "))
list = []
list = [random.randint(0, 100) for i in range(n)]
print(list)
x = int(input("Введите натуральное число: "))
n = ""
while x > 0:
y = str(x % 2)
n = y + n
x = int(x / 2)
print (n)