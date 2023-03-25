#  Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

import random
n = int(input("Введите количество элементов массива: "))
x = int(input("Введите искомое число: "))
my_list = [random.randint(0,10) for i in range(n)]
print(my_list)


min = x - my_list[0]
index = 0
for i in range(1, n):
    count =(x - my_list[index])
    if count <= min:
        min = count
        index = index +1
print('Самый близкий по величине элемент к заданному числу X: -> ', my_list[index])