# 1. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# import itertools
#
# k = int(input('Задайте натуральную степень многочлена k: '))
#
# def get_ratios(k):
#     ratios = [randint(0, 100) for i in range(k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios
#
# def get_polynomial(k, ratios):
#     var = ['*x^'] * (k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')
#
# ratios = get_ratios(k)
# polynom = get_polynomial(k, ratios)
# print(polynom)

# 2. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def remake(equation):
    dictEquation = {}
    equation = equation.replace(' - ', ' -').replace(' + ', ' ')
    equation = equation.split()
    equation = equation[:-2]
    for i in range(len(equation)):
        equation[i] = equation[i].split('x**')
        dictEquation[int(equation[i][1])] = int(equation[i][0])
    return dictEquation

def sumEquation(dict1, dict2):
    dictFinal = {}
    maximum = max(max(dict1), max(dict2))
    for i in range(maximum, -1, -1):
        first = dict1.get(i)
        second = dict2.get(i)
        if first != None or second != None:
            dictFinal[i] = (first if first != None else 0) + (second if second != None else 0)
    return dictFinal

def koefResult(dictFinal):
    result = ''
    for i in dictFinal.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + 'x^' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
        result = result.replace('1x^', 'x^').replace('x^1 ', 'x ').replace('x^0', ' ')
    return result + " = 0"


with open('File1.txt', 'r') as text:
    equation1 = text.readline()
with open('File2.txt', 'r') as text:
    equation2 = text.readline()
dictEquation1 = remake(equation1)
dictEquation2 = remake(equation2)
print(dictEquation1)
print(dictEquation2)
dictFinal = sumEquation(dictEquation1, dictEquation2)
print(dictFinal)
dictFinal = koefResult(dictFinal)
print(dictFinal)
with open('File3.txt', 'w') as text:
    text.writelines(dictFinal)
