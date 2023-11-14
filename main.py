def calk1(a, b):
    return a + b

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calk1, 5, 45)
math(calk2, 5, 45)

math(lambda a, b: a + b, 5, 45)

'''
Задача 1. В списке хранятся числа. 
Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
Пример:
1 2 3 5 8 15 23 38
Ответ:
[(2, 4), (8, 64), (38, 1444)]
'''
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i*i))

print(res)

# Вариант 2 с lambda

def select(f, col):              # map
    return [f(x) for x in col]

def where(f, col):                  # filter
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)

# функция map

list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

"""
Задача: C клавиатуры вводится некий набор чисел, 
в качестве разделителя используется
пробел. Этот набор чисел будет считан в качестве строки. 
Как превратить list строк в list чисел?
"""

data = '15 156 96 3 5 8 52 5'
data = list(map(int, data.split()))
print(data)

# функция filter

data = [15, 65, 9, 33, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

#

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a', encoding='utf-8') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
print(23)

data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()