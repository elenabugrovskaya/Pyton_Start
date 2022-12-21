# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# n = input("Введите число: ")
# n = list(n)
# result = 0
#
# for each_char in n:
#     if each_char == '.':
#         result = result
#     else:
#         each_char = int(each_char)
#         result = result + each_char
# print(result)
# print(list(n))

# 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# my_list = []
# result = 0
# item = 0
# for n in range(1, 5):
#     item = round((1 + 1 / n) ** n, 2)
#     my_list.append(item)
#
# for item in my_list:
#     item = float(item)
#     result = result + item
# print(f'Для n=4 =>',  end=' ')
# print(my_list)
# print(result)

# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование
# библиотеки Random для и получения случайного int.

import random

my_list = []
n = int(input('Введите длину списка: '))
for i in range(n):
    my_list.append(random.randint(0, 20))
print(my_list)

for i in range(n-1):
      temp = my_list[i]
      my_list[i] = my_list[i+1]
      my_list[i+1] = temp
print(my_list)


