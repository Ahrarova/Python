# Задача 2: Найдите сумму цифр трехзначного числа.

n = input("Введите трехзначное число: ")
n = int(n)
 
num1 = n % 10
n = n // 10
num2 = n % 10
n = n // 10
 
print("Сумма цифр числа:", n + num1 + num2 )