# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Введите номер дня недели: '))
if number == 6 and number == 7:
    print("Выходной день")
else:
    print("Рабочий день")

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# for x in [True,False]:
#     for y in [True,False]:
#         for z in [True,False]:
#             print(x,'AND',y,'OR',z,'=',x and y or z)


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# number1 = int(input('Введите x: '))
# number2 = int(input('Введите y: '))
# if number1 > 0 and number2 > 0:
#     print("1 четверть")
# elif number1 < 0 and number2 > 0:
#     print("2 четверть")
# elif number1 < 0 and number2 < 0:
#     print("3 четверть")
# else:
#     print("4 четверть")

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# number = int(input('Введите номер координатной четверти: '))
# if number == 1:
#     print("x > 0; y > 0")
# elif number == 2:
#     print("x < 0; y > 0")
# elif number == 3:
#     print("x < 0; y < 0")
# else:
#     print("x > 0; y < 0")

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# import math
#
# x1 = int(input('Введите x1: '))
# y1 = int(input('Введите y1: '))
# x2 = int(input('Введите x2: '))
# y2 = int(input('Введите y2: '))
#
# print(math.sqrt((x2-x1)**2+(y2-y1)**2))


