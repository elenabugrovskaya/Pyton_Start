# f(x) = -12*x^4*sin(cos(x)) - 18*x^3+5*x^2 + 10*x - 30
# 1 Определить корни
# 2 Найти интервалы, на которых функция возрастает
# 3 Найти интервалы, на которых функция убывает
# 4 Построить график
# 5 Вычислить вершину
# 6 Определить промежутки, на котором f > 0
# 7 Определить промежутки, на котором f < 0

import matplotlib.pyplot as plt
import numpy as np
import sympy

a,b,c,d,e=-12,-18,5,10,-30
def func(x):
    f=a*x**4*np.sin(np.cos(x))-b*x**3+c*x**2 +d*x-e
    return f


limit = 10
step = 0.01
step_acr = 0.000001
color = 'b'
line_style = '-'
direct_up = True


def switch_line():
    global line_style
    if line_style == '-':
        line_style = '-.'
    else:
        line_style = '-'
    return line_style

def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color


x = np.arange(-limit, limit + step, step)

x_change = [(-limit, 'limit')]


for i in range(len(x) - 1):
    if func(x[i]) > 0 and func(x[i + 1]) < 0 or func(x[i]) < 0 and func(x[i + 1]) > 0:
        x_acr = np.arange(x[i], x[i + 1] + step_acr, step_acr) 
        for j in range(len(x_acr) - 1):
            if func(x_acr[j]) > 0 and func(x_acr[j + 1]) < 0 or func(x_acr[j]) < 0 and func(x_acr[j + 1]) > 0:
                x_change.append((x_acr[j], 'zero'))
    if direct_up:
        if func(x[i]) > func(x[i + 1]):
            direct_up = False
            x_change.append((x[i], 'dir'))
    else:
        if func(x[i]) < func(x[i + 1]):
            direct_up = True
            x_change.append((x[i], 'dir'))


x_change.append((limit, 'limit'))


for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.plot(x_change[i][0], func(x_change[i][0]), 'go')
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())

min_y = min(func(x))
min_x = -limit
for x in x_change:
    if x[1] in ['direct','limit']:
        if abs(func(x[0]) - min_y) < abs(min_x - min_y):
            min_x = x[0]

roots = []
for x in x_change:
    if x[1] == 'zero':
        roots.append(str(round(x[0], 2)))
        plt.plot(x[0], func(x[0]), 'gx')

plt.plot(min_x, min_y, 'yo', label=f'Экстремум функции на промежутке [{-limit};{limit}]: ({round(min_x, 2)}, {round(min_y, 2)})')

plt.rcParams['lines.linestyle'] = '-'
plt.plot(0, 0, 'b', label='Убывание > 0')
plt.plot(0, 0, 'r', label='Возрастание > 0')
plt.rcParams['lines.linestyle'] = '--'
plt.plot(0, 0, 'b', label='Убывание < 0')
plt.plot(0, 0, 'r', label='Возрастание < 0')
plt.title(f'Корни на промежутке [{-limit};{limit}]: {", ".join(roots)}')
plt.legend()
plt.grid()
plt.show()

