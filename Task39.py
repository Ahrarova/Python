# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит 
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

import random

list_1 = [random.randint(1,20) for _ in range(int(input('Введите размер 1 списка: ')))]
list_2 = [random.randint(1,20) for _ in range(int(input('Введите размер 2 списка: ')))]

print(list_1)
print(list_2)

final_list = []

for item in list_1:
    if not item in list_2:
        final_list.append(item)

print(final_list)