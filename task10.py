# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input('Введите количество монеток: '))

arms = 0
tails = 0
x = 0
for i in range(n):
    x = random.randint(0,1)
    print(x, end='')
    if x == 0:
        arms += 1
    else:
        tails += 1
if tails > arms:
    print(f'\nпереверните {arms} монет')
else:
    print(f'\nпереверните {tails} монет')