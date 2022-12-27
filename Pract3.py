# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным
# индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
#
# my_list = []
# n = int(input('Введите длину списка: '))
# for i in range(n):
#     my_list.append(random.randint(0, 10))
# print(my_list)
#
# result = 0
# for index in range(len(my_list)):
#     if index % 2 != 0:
#         result = result + my_list[index]
#     else:
#         result = result
# print(result)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# import random
#
# my_list = []
# my_rez = []
# n = int(input('Введите длину списка: '))
# if n > 0:
#     for i in range(n):
#         my_list.append(random.randint(0, 10))
#     print(my_list)
#
#     l = len(my_list) // 2 + 1 if len(my_list) % 2 != 0 else len(my_list) // 2
#     for i in range(round(l)):
#         my_rez.append(my_list[i] * my_list[-1-i])
#     print(my_rez)
# else:
#     breakpoint()

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной
# части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# my_ostatok = []
# rez = 0
# for el in my_list:
#     ostatok = el - int(el)
#     round(ostatok, 2)
#     if ostatok != 0:
#         my_ostatok.append(round(ostatok, 2))
# rez = max(my_ostatok) - min(my_ostatok)
# print(rez)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# n = int(input('Введите число N: '))
# b = ''
#
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
#
# print(b)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


fib1 = 1
fib2 = -1
n = int(input('Задайте число: '))
my_list = [fib1, fib2]

for i in range(2, n):
    fib1, fib2 = fib2, fib1 - fib2
    my_list.append(fib2)
my_list = my_list[::-1]

fib1 = fib2 = 1
my_list1 = [0, fib1, fib2]
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    my_list1.append(fib2)
my_list = my_list + my_list1
print(my_list)


