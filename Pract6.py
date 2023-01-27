# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование
# библиотеки Random для и получения случайного int.

# import random
# n = int(input('Введите длину списка: '))
# my_list = [random.randint(0, 20) for i in range(n)]
# print(my_list)
# shuffle_list = sorted(my_list, key=lambda A: random.random())
# print(shuffle_list)

# Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# my_list = [round((1 + 1 / n) ** n, 2) for n in range(1, 5)]
# result = sum(my_list)
# print(f'Для n=4 => {my_list} \nCумма = {result}')


# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# num = input("Введите вещественное число: ")
# result = sum(map(int, num.replace('.', '')))
# print(result)

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным
# индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint as RI
# n = int(input('Введите длину списка: '))
# my_list = [RI(0, 10) for i in range(n)]
# print(my_list)
# print(sum(my_list[1::2]))

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math
from random import randint as RI
n = int(input('Введите длину списка: '))
my_list = [RI(0, 10) for i in range(n)]
print(my_list)
print(list([a*b for a, b in zip(my_list[0:math.ceil(len(my_list)/2)], my_list[::-1])]))
