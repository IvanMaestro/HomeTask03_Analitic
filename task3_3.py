# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform


def init_list(count):
    ls = []
    for i in range(count):
        ls.append(round(uniform(0, 10), 2))
    return ls


def min_max_diff(some_list):
    for i in range(len(some_list)):
        some_list[i] = round(some_list[i] % 1, 2)
    max_el = max(some_list)
    min_el = min(some_list)
    return f'Min: {min_el}, Max: {max_el}. Difference: {round(max_el - min_el, 2)}'


n = int(input('Задайте размер списка: '))
while n < 0:
    n = int(input('Размер списка должен быть болбше нуля: '))
input_list = init_list(n)
print(input_list)

print(min_max_diff(input_list))