# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import sample


def init_list(count):
    ls = sample(range(count*2), count)
    return ls


def elem_sum(new_list):
    res = 0
    for i in range(len(new_list)):
        if i % 2 == 1:
            res += new_list[i]
    return res

# 1 вариант в 2 метода
n = int(input('Задайте размер списка: '))
while n < 0:
    n = int(input('Размер списка должен быть болбше нуля: '))
input_list = init_list(n)
print(f'{input_list}, \nСумма элементов на нечетных индексах -> {elem_sum(input_list)}')


# 2 вариант - покороче
n = int(input('Задайте размер списка: '))
input_list = init_list(n)
sum1 = 0
for i in range(1, len(input_list), 2):
    sum1 += input_list[i]
print(f"{input_list} -> сумма элементов на нечётных индексах равна: {sum1}")

